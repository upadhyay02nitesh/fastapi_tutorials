from fastapi import FastAPI, Depends, HTTPException, status, Request, Form,Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from sqlalchemy.orm import Session
from model import User
from auth import verify_password
from db_connection import get_db
from pydantic import BaseModel
from schema import UserCreate
from auth import hash_password, verify_password
from typing import List
# FastAPI app
app = FastAPI()

# Secret key to encode/decode JWT
SECRET_KEY = "fastapi-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# OAuth2 scheme for token extraction from request header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Pydantic model for token response
class Token(BaseModel):
    access_token: str
    token_type: str

# Pydantic model for token data (payload content)
class TokenData(BaseModel):
    username: Optional[str] = None

class UserOut(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

# Authenticate user with DB and verify password
def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

# Create JWT token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Dependency to get current user from token
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")  # 'sub' is a standard JWT claim for subject/user
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.username == token_data.username).first()
    if user is None:
        raise credentials_exception
    return user

@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    user_obj = User(username=user.username, hashed_password=hash_password(user.password))
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return {"message": "User registered successfully"}
# Token endpoint for login, returns JWT token on successful auth
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Protected profile endpoint, requires valid JWT token
@app.get("/profile")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return {
        "username": current_user.username,
        "message": f"🎉 Congratulations, {current_user.username}! Welcome to your profile page.",
        "timestamp": datetime.utcnow().isoformat()
    }
@app.get("/logout")
def logout():
    return {"message": "Logout by clearing the token on client side"}

@app.get("/pagination",response_model=List[UserOut])
async def get_paginated_users(request: Request,page:int, db: Session = Depends(get_db)):
    # page = int(request.query_params.get("page", 1))  # default page 1
    # page = page # default page 1
    limit = 2  # fixed items per page
    offset = (page - 1) * limit

    users = db.query(User).offset(offset).limit(limit).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")

    return users

@app.get("/fast-pagination", response_model=List[UserOut])
async def fast_paginated_users(last_id: Optional[int] = Query(None),  # last seen user ID (for next page)
db: Session = Depends(get_db)):
    limit = 2  # fixed items per page

    query = db.query(User)

    if last_id:
        query = query.filter(User.id > last_id)  # only rows after last seen id
        print(query)

    users = query.order_by(User.id).limit(limit).all()

    if not users:
        raise HTTPException(status_code=404, detail="No users found")

    return users
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI, Request, Depends, Form, HTTPException,Response
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from model import User
from schema import UserCreate, UserOut
from auth import hash_password, verify_password
from fastapi.middleware.cors import CORSMiddleware
from db_connection import get_db
from fastapi.responses import JSONResponse
from starlette.status import HTTP_302_FOUND
from datetime import datetime
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="fastapi-secret-key",max_age=3600)

# Add CORSMiddleware for CORS (cross-origin requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Or specify your frontend domain here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

@app.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    print("Username received:", username)
    print("Password received:", password)

    user = db.query(User).filter(User.username == username).first()
    print("User from DB:", user)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    request.session["user_id"] = user.id
    return {"message": "Login successful"}

@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return {"message": "Logged out successfully"}

@app.get("/profile", response_model=UserOut)
def profile(request: Request, db: Session = Depends(get_db)):
    print("SESSION:", request.session)
    print("HEADERS:", request.headers)

    user_id = request.session.get("user_id")
    user = db.query(User).filter(User.id == user_id).first()
    client_host = request.client.host
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    return JSONResponse(status_code=200,
    content={
        "status":"success",
        "message": f"""
        🎉 Congratulations, {user.username}!  
        Welcome to your profile page.  

        🌐 Your current IP address is: {client_host}  

        We're excited to have you here—explore your dashboard and make the most out of your experience! 🚀
            """
,
        "timestamp":datetime.now().isoformat()
    })

@app.get("/set-cookie")
def set_cookie(response: Response):
    response.set_cookie(key="mycookie", value="nitesh123", max_age=3600)
    return {"message": "Cookie set!"}

# Read cookie from request
@app.get("/get-cookie")
def get_cookie(request: Request):
    cookie_value = request.cookies.get("mycookie")
    if cookie_value:
        return {"cookie_value": cookie_value}
    else:
        return JSONResponse(status_code=404, content={"message": "Cookie not found"})

# Delete cookie
@app.get("/delete-cookie")
def delete_cookie(response: Response):
    response.delete_cookie("mycookie")
    return {"message": "Cookie deleted"}
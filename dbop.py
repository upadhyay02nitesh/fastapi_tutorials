from fastapi import FastAPI, HTTPException,Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session

# Initialize FastAPI app
app = FastAPI()

# Database configuration
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:Rewa%401234@localhost:3306/fastapi_db"


# Create an SQLAlchemy engine and session maker
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base model for SQLAlchemy
Base = declarative_base()

# Define the model (table structure)
class Tea(Base):
    __tablename__ = "tea"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    salary = Column(Float)

# Create the table (if it doesn't already exist)
Base.metadata.create_all(bind=engine)

# Pydantic model for data validation
class TeaCreate(BaseModel):
    name: str
    salary: float

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes
@app.post("/tea/")
async def create_tea(tea: TeaCreate, db: Session = Depends(get_db)):
    db_tea = Tea(name=tea.name, salary=tea.salary)
    db.add(db_tea)
    db.commit()
    db.refresh(db_tea)
    return db_tea

@app.get("/tea/{tea_id}")
async def read_tea(tea_id: int, db: Session = Depends(get_db)):
    db_tea = db.query(Tea).filter(Tea.id == tea_id).first()
    if db_tea is None:
        raise HTTPException(status_code=404, detail="Tea not found")
    return db_tea

@app.get("/tea/")
async def get_all_tea(db: Session = Depends(get_db)):
    return db.query(Tea).all()

@app.put("/tea/{tea_id}")
async def update_tea(tea_id: int,updated_tea:TeaCreate, db: Session = Depends(get_db)):
    db_tea = db.query(Tea).filter(Tea.id == tea_id).first()
    if db_tea is None:
        raise HTTPException(status_code=404, detail="Tea not found")
    else:
        db_tea.name=updated_tea.name
        db_tea.salary=updated_tea.salary

        db.commit()
        db.refresh(db_tea)
        return db_tea

@app.delete("/tea/{tea_id}")
async def delete_tea(tea_id: int, db: Session = Depends(get_db)):
    db_tea = db.query(Tea).filter(Tea.id == tea_id).first()
    if db_tea is None:
        raise HTTPException(status_code=404, detail="Tea not found")
    else:
        db.delete(db_tea)
        db.commit()
        return {"message": f"User {tea_id} deleted successfully"}
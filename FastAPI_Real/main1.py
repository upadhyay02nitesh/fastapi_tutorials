# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from db_connection import SessionLocal,engine   
from model import Base, Tea
from schema import TeaCreate


# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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
async def update_tea(tea_id: int, updated_tea: TeaCreate, db: Session = Depends(get_db)):
    db_tea = db.query(Tea).filter(Tea.id == tea_id).first()
    if db_tea is None:
        raise HTTPException(status_code=404, detail="Tea not found")
    db_tea.name = updated_tea.name
    db_tea.salary = updated_tea.salary
    db.commit()
    db.refresh(db_tea)
    return db_tea

@app.delete("/tea/{tea_id}")
async def delete_tea(tea_id: int, db: Session = Depends(get_db)):
    db_tea = db.query(Tea).filter(Tea.id == tea_id).first()
    if db_tea is None:
        raise HTTPException(status_code=404, detail="Tea not found")
    db.delete(db_tea)
    db.commit()
    return {"message": f"User {tea_id} deleted successfully"}

from sqlalchemy import Column, Integer, String
from db_connection import Base
from db_connection import engine

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100))
Base.metadata.create_all(bind=engine)
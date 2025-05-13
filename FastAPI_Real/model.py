# models.py
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Tea(Base):
    __tablename__ = "tea"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    salary = Column(Float)

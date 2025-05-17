# models.py
from sqlalchemy import Column, Integer, String, Float,ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()

class Tea(Base):
    __tablename__ = "tea"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    salary = Column(Float)

class DeletedTea(Base):
    __tablename__ = "deleted_tea"
    id = Column(Integer, primary_key=True, index=True)
    tea_id = Column(Integer)  # Foreign key to original tea table
    name = Column(String(255))
    salary = Column(Float)
    deleted_at = Column(DateTime, default=datetime.utcnow)  # Timestamp of deletion
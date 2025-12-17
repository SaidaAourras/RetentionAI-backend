from .base import Base
from sqlalchemy import Column , Integer , String , Date 
from datetime import datetime
from sqlalchemy.orm import relationship 



class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer , primary_key=True , index=True)
    username = Column(String , nullable=False , unique=True)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String , nullable=False)
    createdAt = Column(Date , default= datetime.utcnow)
    
    prediction_history = relationship("Prediction_history" , back_populates="user" , cascade="all, delete")
    
   
    
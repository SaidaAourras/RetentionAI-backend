from .base import Base
from sqlalchemy import Column , Integer , String 
from sqlalchemy.orm import relationship 



class Employee(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer , primary_key=True , index=True)
    name = Column(String)
    age = Column(Integer)
    role = Column(String)
    
    prediction_history = relationship("Prediction_history" , back_populates="employee")
    
   
    
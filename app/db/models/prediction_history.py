from .base import Base
from sqlalchemy import Column , Integer , ForeignKey  , DateTime
from datetime import datetime
from sqlalchemy.orm import relationship 



class Prediction_history(Base):
    __tablename__ = 'predictions_history'
    
    id = Column(Integer , primary_key=True , index=True)
    probability = Column(Integer)
    createdAt = Column(DateTime , default= datetime.utcnow)
    
    user_id = Column(Integer , ForeignKey("users.id"))
    employee_id = Column(Integer , ForeignKey("employees.id"), unique=True)
    
    user = relationship("User" , back_populates='predictions_history')
    employee = relationship("Employee" , back_populates="predictions_history")
    
   
    
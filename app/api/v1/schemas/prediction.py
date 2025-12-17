from pydantic import BaseModel
from datetime import datetime

class PredictionBase(BaseModel):
    probability: int
    

class PredcitionCreate(PredictionBase):
    user_id: int
    employee_id: int
    

class PredictionResponse(PredictionBase):
    id: int
    createdAt: datetime
    
    class Config:
        from_attributes = True

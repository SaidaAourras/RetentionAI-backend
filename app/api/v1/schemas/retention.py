from pydantic import BaseModel


class RetentionBase(BaseModel):
    churn_probability : float
    employe_id: int
    

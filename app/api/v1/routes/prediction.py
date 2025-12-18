from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from app.api.v1.dependencies import get_db
from app.api.v1.schemas.employee import EmployeBase
from app.services.user_services import verify_user_is_exists
import joblib
import pandas as pd
from app.db.models.employee import Employee
from app.db.models.user import User
from app.db.models.prediction_history import Prediction_history




model = joblib.load('ml/models/logistic_regression_model.pkl')

predecit_router = APIRouter(prefix='/predict', tags=['prediction'])

@predecit_router.post('/predict')
def predict_Attrition(employee:EmployeBase , db: Session = Depends(get_db)):
    
    employee_dict = employee.model_dump()
    
    employee_df = pd.DataFrame([employee_dict])
    
    prediction = model.predict_proba(employee_df)
    
    probability = round(float(prediction[0,1]),2)
    
    print(probability)
    
    new_employee = create_employee(employee , db)
    
    fake_user = User(
        id = 1,
        email = "user@example.com",
        username = "string",
        password_hash = "$argon2id$v=19$m=65536,t=3,p=4$9bNgbiBWrmOtg45Dj4yUKw$B5OmhimRWkQH5wooWdE6Sw5Lm4cAj6QFhFgYQIUkIPQ",
        createdAt = "2025-12-18"
    )
    current_user = verify_user_is_exists(fake_user , db)
    
    create_history(current_user.id , new_employee.id  , probability , db)
    
    return {
        "churn_probability " : probability
    }


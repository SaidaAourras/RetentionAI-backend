from fastapi import APIRouter , Depends , HTTPException , status
from sqlalchemy.orm import Session
from app.api.v1.dependencies import get_db
from app.api.v1.schemas.employee import EmployeBase
import joblib
import pandas as pd
from app.services.employee_services import create_employee
from app.services.history_prediction_services import create_history
from app.services.auth_services import verify_token



model = joblib.load('ml/models/logistic_regression_model.pkl')

predecit_router = APIRouter(prefix='/predict', tags=['prediction'])

@predecit_router.post('/predict')
def predict_Attrition(employee:EmployeBase , db: Session = Depends(get_db) , current_user : dict  = Depends(verify_token)):
    
    user_id = current_user.get("sub")
    
    if not user_id:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="token invalide"
        )
        
    employee_dict = employee.model_dump()
    employee_df = pd.DataFrame([employee_dict])
    
    prediction = model.predict_proba(employee_df)
    probability = round(float(prediction[0,1]),2)
    
    print(probability)
    
    new_employee = create_employee(employee , db)
    
    create_history(user_id , new_employee.id  , probability , db)
    
    return {
        "churn_probability " : probability,
        "employe_id": new_employee.id
    }


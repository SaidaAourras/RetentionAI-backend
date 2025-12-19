from fastapi import APIRouter , Depends , HTTPException , status
from sqlalchemy.orm import Session
from app.api.v1.dependencies import get_db
from app.api.v1.schemas.retention import RetentionBase
import joblib
import pandas as pd
from app.services.retention_services import retention_employe
from app.db.models.employee import Employee
from app.services.auth_services import verify_token




model = joblib.load('ml/models/logistic_regression_model.pkl')

retention_router = APIRouter(prefix='/retention', tags=['Retention'])

@retention_router.post('/generate-retention-plan')
def predict_Attrition(requestRetention : RetentionBase , db: Session = Depends(get_db) , current_user : dict  = Depends(verify_token)):
    
    
    user_id = current_user.get("sub")
    
    if not user_id:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="token invalide"
        )
    
    employee = db.query(Employee).filter(Employee.id == requestRetention.employe_id).first()
    
    
    if requestRetention.churn_probability >= 50 :
        result = retention_employe(employee)
        return result
    else:
        return {'response':'pas de risque'}


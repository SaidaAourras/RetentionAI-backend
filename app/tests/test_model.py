import joblib
import pandas as pd

def test_model_prediction():
    
    model = joblib.load('ml/models/logistic_regression_model.pkl')
    
    employee_data = pd.DataFrame([{
        "Age": 35, "BusinessTravel": "Travel_Rarely", "Department": "Sales", "Education": 3,
        "EducationField": "Life Sciences", "EnvironmentSatisfaction": 3, "Gender": "Male",
        "JobInvolvement": 3, "JobLevel": 2, "JobRole": "Sales Executive", "JobSatisfaction": 3,
        "MaritalStatus": "Single", "MonthlyIncome": 5000, "OverTime": "No", "PerformanceRating": 3,
        "RelationshipSatisfaction": 3, "StockOptionLevel": 0, "TotalWorkingYears": 10,
        "WorkLifeBalance": 3, "YearsAtCompany": 5, "YearsInCurrentRole": 2, "YearsWithCurrManager": 2
    }])
    
    proba = model.predict_proba(employee_data)[0][1]
    
    assert isinstance(proba, float)
    assert 0.0 <= proba <= 1.0


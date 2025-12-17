from pydantic import BaseModel

class EmployeBase(BaseModel):
    Age : int
    BusinessTravel:str
    Department: str
    Education:int
    EducationField: str
    EnvironmentSatisfaction:int
    Gender:str
    JobInvolvement: int
    JobLevel:int
    JobRole:str
    JobSatisfaction:int
    MaritalStatus: str
    MonthlyIncome: int
    OverTime:str
    PerformanceRating: int
    RelationshipSatisfaction: int
    StockOptionLevel: int
    TotalWorkingYears: int
    WorkLifeBalance: int
    YearsAtCompany:int
    YearsInCurrentRole: int
    YearsWithCurrManager: int
    
# response
    
class EmployeResponse(EmployeBase):
    id: int
        
    class Config:
        from_attributes = True
    
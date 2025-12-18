from .base import Base
from sqlalchemy import Column , Integer , String 
from sqlalchemy.orm import relationship 



class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    Age = Column(Integer, nullable=False)
    BusinessTravel = Column(String, nullable=False)
    Department = Column(String, nullable=False)
    Education = Column(Integer, nullable=False)
    EducationField = Column(String, nullable=False)
    EnvironmentSatisfaction = Column(Integer, nullable=False)
    Gender = Column(String, nullable=False)
    JobInvolvement = Column(Integer, nullable=False)
    JobLevel = Column(Integer, nullable=False)
    JobRole = Column(String, nullable=False)
    JobSatisfaction = Column(Integer, nullable=False)
    MaritalStatus = Column(String, nullable=False)
    MonthlyIncome = Column(Integer, nullable=False)
    OverTime = Column(String, nullable=False)
    PerformanceRating = Column(Integer, nullable=False)
    RelationshipSatisfaction = Column(Integer, nullable=False)
    StockOptionLevel = Column(Integer, nullable=False)
    TotalWorkingYears = Column(Integer, nullable=False)
    WorkLifeBalance = Column(Integer, nullable=False)
    YearsAtCompany = Column(Integer, nullable=False)
    YearsInCurrentRole = Column(Integer, nullable=False)
    YearsWithCurrManager = Column(Integer, nullable=False)
    
    prediction_history = relationship("Prediction_history" , back_populates="employee")
    
   
    
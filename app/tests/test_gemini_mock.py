from app.services.retention_services import retention_employe
from app.db.models.employee import Employee

def test_retention_employe_with_mocked_gemini(mocker):
    
    fake_response = mocker.Mock()
    fake_response.text = """
    {
      "retention_plan":[
        "Proposer 2 jours de télétravail",
        "Réévaluer la charge de déplacement",
        "Plan de formation personnalisé"
      ]
    }
    """
    
    fake_client = mocker.Mock()
    fake_client.models.generate_content.return_value = fake_response
    
    mocker.patch("app.services.retention_services.genai.Client",return_value=fake_client)
    
    employee = Employee(
    Age='35',
    BusinessTravel='Travel_Rarely',
    Department='Sales', 
    Education='3',
    EducationField='Life Sciences', 
    EnvironmentSatisfaction='3', 
    Gender='Male',
    JobInvolvement='3', 
    JobLevel='2', 
    JobRole='Sales Executive', 
    JobSatisfaction='3',
    MaritalStatus='Single', 
    MonthlyIncome='5000', 
    OverTime='No', 
    PerformanceRating='3',
    RelationshipSatisfaction='3',
    StockOptionLevel='0', 
    TotalWorkingYears='10',
    WorkLifeBalance='3', 
    YearsAtCompany='5', 
    YearsInCurrentRole='2', 
    YearsWithCurrManager='2'
    )
    
    result = retention_employe(employee)
    
    assert "retention_plan" in result
    assert isinstance(result["retention_plan"], list)
    assert len(result["retention_plan"]) > 0

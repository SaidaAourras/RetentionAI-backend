from dotenv import load_dotenv
from google import genai
from app.db.models.employee import Employee
import json
import os

load_dotenv()

API_KEY_GEMINI = os.getenv('API_KEY_GEMINI')


# create prompt
def create_prompt(employee):
    prompt = f"""
                Agis comme un expert RH senior spécialisé dans la rétention des talents.

                Voici les informations complètes sur l’employé :

                - Âge : {employee.Age}
                - Genre : {employee.Gender}
                - Statut marital : {employee.MaritalStatus}

                - Département : {employee.Department}
                - Rôle : {employee.JobRole}
                - Niveau de poste : {employee.JobLevel}
                - Implication dans le travail : {employee.JobInvolvement}/4
                - Années d'expérience totale : {employee.TotalWorkingYears}

                - Niveau d'éducation : {employee.Education}
                - Domaine d'éducation : {employee.EducationField}

                - Satisfaction au travail : {employee.JobSatisfaction}/4
                - Satisfaction de l'environnement : {employee.EnvironmentSatisfaction}/4
                - Satisfaction relationnelle : {employee.RelationshipSatisfaction}/4
                - Équilibre vie professionnelle / personnelle : {employee.WorkLifeBalance}/4

                - Déplacements professionnels : {employee.BusinessTravel}
                - Heures supplémentaires : {employee.OverTime}
                - Revenu mensuel : {employee.MonthlyIncome}
                - Niveau d'options sur actions : {employee.StockOptionLevel}

                - Ancienneté dans l'entreprise : {employee.YearsAtCompany} ans
                - Ancienneté dans le rôle actuel : {employee.YearsInCurrentRole} ans
                - Ancienneté avec le manager actuel : {employee.YearsWithCurrManager} ans

                - Évaluation de la performance : {employee.PerformanceRating}/4

                Contexte :
                Ce salarié présente un **risque élevé de départ (churn_probability)** selon le modèle de machine learning.

                Tâche :
                Propose exactement **3 actions concrètes, personnalisées et réalistes** pour retenir cet employé.

                Règles de sortie (OBLIGATOIRES) :
                - Retourne UNIQUEMENT un JSON valide
                - Aucune phrase hors du JSON
                - Le format doit être STRICTEMENT :

                {{
                    
                "retention_plan": [
                    "Action 1",
                    "Action 2",
                    "Action 3"
                ]
                }}

                - Les actions doivent être courtes, claires et directement actionnables par un manager RH.
                """

    return prompt




# API IA Générative
def retention_employe(employee):
    
    prompt = create_prompt(employee)
    
    try:
        client = genai.Client(api_key=API_KEY_GEMINI)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
            "response_mime_type" : "application/json"
        }
        )
        
        result = json.loads(response.text)
        return result
    except Exception as e:
        return {'erreur':f'Gemini analysis failed {e}'}
    

# employee = Employee(
#         Age= 42,
#         BusinessTravel= "Travel_Frequently",
#         Department= "Research & Development",
#         Education= 3,
#         EducationField= "Life Sciences",
#         EnvironmentSatisfaction= 2,
#         Gender= "Male",
#         JobInvolvement= 3,
#         JobLevel= 2,
#         JobRole= "Research Scientist",
#         JobSatisfaction= 2,
#         MaritalStatus= "Married",
#         MonthlyIncome= 6200,
#         OverTime= "Yes",
#         PerformanceRating= 3,
#         RelationshipSatisfaction= 3,
#         StockOptionLevel= 1,
#         TotalWorkingYears= 15,
#         WorkLifeBalance= 2,
#         YearsAtCompany= 9,
#         YearsInCurrentRole= 6,
#         YearsWithCurrManager= 4
# )

# prompt = create_prompt(employee)
# print(analyse_with_gemini(prompt))
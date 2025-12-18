from app.db.models.prediction_history import Prediction_history

# create history

def create_history(userid , employeeid  , proba , db):
    
    new_history = Prediction_history(
        user_id = userid ,
        employee_id = employeeid,
        probability = proba
    )
    
    db.add(new_history)
    db.commit()
    db.refresh(new_history)
    
    return new_history
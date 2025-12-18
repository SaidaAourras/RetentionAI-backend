from app.db.models.employee import Employee


# create employee

def create_employee(employee , db):
    new_employee = Employee(**employee.model_dump())
    
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    
    return new_employee
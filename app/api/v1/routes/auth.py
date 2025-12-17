from fastapi import APIRouter , Depends  , HTTPException
from sqlalchemy.orm import Session
from ..schemas.user import UserCreate , LoginRequest , UserResponse
from ..dependencies import get_db
from app.services.user_services import create_user , verify_user_is_exists
# from app.services.auth_service import verify_token , create_token


auth_router = APIRouter(prefix='/auth' ,tags=["authentication"])


@auth_router.post('/register')
def register(user:UserCreate , db:Session=Depends(get_db)):
    
    user_exists = verify_user_is_exists(user , db)
    
    if user_exists:
        raise HTTPException(
        status_code=400,
        detail="Email deja exists"
    )
        
    else:
        return create_user(user , db)
    
    


@auth_router.post('/login' )
def login(user:LoginRequest , db:Session = Depends(get_db)):
    user_exists = verify_user_is_exists(user , db)
    if user_exists:
        user_dict = user.model_dump()
        return user_dict
            
    raise HTTPException(
        status_code=401,
        detail="Email ou mot de passe incorrect"
    )


# @auth_router.post("/logout")
# def logout():
#     return {"message": "OK"}
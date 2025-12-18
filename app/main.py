from fastapi import FastAPI
from app.db.database import engine
from app.db.models.base import Base
from app.api.v1.routes.auth import auth_router
from app.api.v1.routes.prediction import predecit_router
from app.api.v1.routes.retnetion import retention_router
from core.cors import setup_cors

app = FastAPI()
setup_cors(app)

Base.metadata.create_all(engine)

app.include_router(auth_router , prefix='/api/v1')
app.include_router(predecit_router , prefix='/api/v1')
app.include_router(retention_router , prefix='/api/v1')
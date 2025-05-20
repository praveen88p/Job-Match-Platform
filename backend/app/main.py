from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database
from .routes import auth_routes
from .routes import auth_routes, profile_routes
# In Python shell or FastAPI startup file
from .models import Base
from .database import engine
from .routes import job_routes
from .routes import job_routes

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_routes.router)
app.include_router(profile_routes.router)
app.include_router(job_routes.router)

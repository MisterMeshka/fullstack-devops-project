from .routers import users
from fastapi import Depends, FastAPI, HTTPException
from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import Base, engine, get_db

app = FastAPI()


@app.get("/")
def root():
    return {"message": "DevOps Project is running!"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/db")
def db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        return {"postgres": result.scalar()}

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
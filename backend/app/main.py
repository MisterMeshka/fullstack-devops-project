from fastapi import FastAPI
from sqlalchemy import create_engine, text
import os

app = FastAPI()

DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

engine = create_engine(DATABASE_URL)


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
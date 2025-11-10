import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "devkey")
    DB_USER = os.getenv("DATABASE_USER", "root") # Usuario do banco
    DB_PASS = os.getenv("DATABASE_PASSWORD", "") #Senha declaradda no .env
    DB_HOST = os.getenv("DATABASE_HOST", "127.0.0.1")
    DB_PORT = os.getenv("DATABASE_PORT", "3306")
    DB_NAME = os.getenv("DATABASE_NAME", "brilhance_db")
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

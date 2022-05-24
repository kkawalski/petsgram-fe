import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your-super-secret-key")
    API_URL = os.getenv("API_URL", "http://127.0.0.1:5001")

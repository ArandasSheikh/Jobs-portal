
    
class Settings:
    DATABASE_URL = "mysql+pymysql://root:Mnbvcx$12345678@127.0.0.1:3307/FASTAPI"
    SECRET_KEY = "supersecretkey"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

settings = Settings()

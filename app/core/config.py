from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    postgres_username: str 
    postgres_password: str
    postgres_hostname: str
    postgres_port: str
    postgres_dbname: str
    
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
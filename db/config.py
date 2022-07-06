from pydantic import BaseSettings


class Settings(BaseSettings):
    database_name: str = "test_db"
    db_username: str = "root"
    db_password: str = "W@lcom@r36@"
    host: str = "127.0.0.1"
    ports: int = "3306"
   

    # class Config:
    #     env_file = ".env"

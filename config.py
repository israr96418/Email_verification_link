from pydantic import BaseSettings

class Setting(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    class Config:
        env_file = ".env"

setting = Setting()
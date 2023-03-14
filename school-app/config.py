import os
from pydantic import BaseSettings
from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))


class DBConfig(BaseSettings):
    MYSQL_HOST: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DB: str

    class Config:
        env_file = '.env'


database_settings = DBConfig()

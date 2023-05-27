from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .utilities.config_utils import load_config, db_uri
from os import getenv
import dotenv
dotenv.load_dotenv()

db_conf = load_config("./credentials.yaml")["sql_database"]
SQLALCHEMY_DATABSE_URL = db_uri(**db_conf)

engine = create_engine(SQLALCHEMY_DATABSE_URL)  # a gate connect to the database
session_local = sessionmaker(
    autocommit=False,  # not auto commit changes to the database
    autoflush=False,  # not flush pending changes to the database => more control => more errors-prone
    bind=engine,  # connect to the database through the var `engine`
)
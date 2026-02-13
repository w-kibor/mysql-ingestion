import os
import urllib.parse
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

def get_db_engine():
    """Creates and returns a SQLAlchemy engine for the MySQL database."""
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    # URL encode the password to handle special characters securely
    encoded_password = urllib.parse.quote_plus(db_password)

    db_url = (
        f"mysql+pymysql://{db_user}:{encoded_password}"
        f"@{db_host}:{db_port}/{db_name}"
    )
    
    return create_engine(db_url)

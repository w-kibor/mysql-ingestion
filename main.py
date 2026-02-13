import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from sqlalchemy import text
import sys

load_dotenv()

import urllib.parse

# Connection string using environment variables
password = urllib.parse.quote_plus(os.getenv('DB_PASSWORD'))
db_url = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{password}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
engine = create_engine(db_url)

def ingest_data(file_path):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        print(f"Data read successfully from {file_path}")

        # Ingest data into MySQL
        df.to_sql('hn_reader', con=engine, if_exists='append', index=False)
        print("Data ingested successfully into MySQL")
    except Exception as e:
        print(f"Error during data ingestion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    file_path = 'data.csv'
    if os.path.exists(file_path):
        ingest_data(file_path)
    else:
        print(f"File {file_path} not found.")
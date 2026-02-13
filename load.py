import pandas as pd
from sqlalchemy.engine import Engine

def load_data(df, engine, table_name='articles'):
    """
    Loads the DataFrame into the MySQL database.
    
    Args:
        df (pd.DataFrame): The transformed DataFrame.
        engine (sqlalchemy.engine.Engine): The database connection engine.
        table_name (str): The name of the target table.
    """
    print(f"Loading {len(df)} rows into table '{table_name}'...")
    try:
        df.to_sql(table_name, con=engine, if_exists='append', index=False)
        print("✅ Data ingested successfully!")
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        raise

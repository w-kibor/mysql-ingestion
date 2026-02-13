import sys
from database import get_db_engine
from extract import fetch_hn_top_stories
from transform import transform_data
from load import load_data

def main():
    try:
        # 1. Setup Database Connection
        engine = get_db_engine()
        
        # 2. Extract from HN API
        print("Starting ETL pipeline...")
        raw_data = fetch_hn_top_stories(limit=50)
        
        if not raw_data:
            print("No data fetched. Exiting.")
            return

        # 3. Transform
        df_cleaned = transform_data(raw_data)
        
        # 4. Load
        load_data(df_cleaned, engine)
        
    except Exception as e:
        print(f"Pipeline failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
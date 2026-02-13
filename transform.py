import pandas as pd

def transform_data(data):
    """
    Cleans and transforms the raw data (DataFrame or list of dicts) to match the database schema.
    
    Args:
        data (pd.DataFrame or list[dict]): The raw data.
        
    Returns:
        pd.DataFrame: The transformed DataFrame.
    """
    print("Transforming data...")
    
    # Convert list of dicts to DataFrame if necessary
    if isinstance(data, list):
        df = pd.DataFrame(data)
    else:
        df = data.copy()

    # 1. Rename columns to match SQL schema
    # HN API keys: 'by', 'time', 'url', 'score', 'title'
    mapping = {
        'by': 'author', 
        'time': 'posted_at', 
        'url': 'url', 
        'score': 'score', 
        'title': 'title'
    }
    df = df.rename(columns=mapping)

    # 2. Convert Unix Timestamp (seconds) to MySQL Datetime
    if 'posted_at' in df.columns:
        df['posted_at'] = pd.to_datetime(df['posted_at'], unit='s')

    # 3. Add default category if it doesn't exist
    if 'category' not in df.columns:
        df['category'] = 'Tech'

    # 4. Filter to only include columns expected in the SQL table
    valid_columns = ['id', 'title', 'url', 'author', 'score', 'posted_at', 'category']
    
    # Select only columns that exist in the DataFrame
    # Re-order them to match preference if desired, but set intersection is safer
    cols_to_keep = [col for col in valid_columns if col in df.columns]
    
    # Handle cases where some stories might be missing 'url' (e.g. Ask HN)
    # We can fillna or just let them be null if DB allows. 
    # Let's ensure 'url' exists even if empty for consistency
    if 'url' not in df.columns:
        df['url'] = None
        if 'url' in valid_columns:
            cols_to_keep.append('url')
            
    return df[cols_to_keep]

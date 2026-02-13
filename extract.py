import pandas as pd
import requests
import time

def extract_data(file_path=None):
    """
    Reads data from a CSV file.
    
    Args:
        file_path (str): The path to the CSV file.
        
    Returns:
        pd.DataFrame: A pandas DataFrame containing the raw data.
    """
    # ... existing CSV logic ...
    pass 

def fetch_hn_top_stories(limit=50):
    """
    Fetches the top `limit` stories from Hacker News API.
    
    Returns:
        list[dict]: A list of dictionaries containing raw story data.
    """
    base_url = "https://hacker-news.firebaseio.com/v0"
    
    try:
        # 1. Get Top Story IDs
        print(f"Fetching top {limit} story IDs...")
        response = requests.get(f"{base_url}/topstories.json")
        response.raise_for_status()
        top_ids = response.json()[:limit]
        
        stories = []
        print(f"Fetching details for {len(top_ids)} stories...")
        
        # 2. Fetch details for each story
        for i, story_id in enumerate(top_ids):
            # rate limiting prevention
            if i % 10 == 0:
                print(f"Processed {i}/{limit}...")
            
            try:
                story_resp = requests.get(f"{base_url}/item/{story_id}.json")
                story_resp.raise_for_status()
                story_data = story_resp.json()
                
                # Only keep stories (files out comments, jobs if they appear in topstories)
                if story_data and story_data.get('type') == 'story':
                    stories.append(story_data)
            except Exception as e:
                print(f"Failed to fetch story {story_id}: {e}")
                continue
                
        print(f"Successfully fetched {len(stories)} stories.")
        return stories
        
    except Exception as e:
        print(f"Error fetching data from HN API: {e}")
        return []

# Keep the original function for backward compatibility if needed, 
# or we can remove it if we strictly switch to API. 
# For now, I'll keep the file_path version as a fallback or alternative.
def extract_data_from_csv(file_path):
    import os
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print(f"Reading data from {file_path}...")
    return pd.read_csv(file_path)


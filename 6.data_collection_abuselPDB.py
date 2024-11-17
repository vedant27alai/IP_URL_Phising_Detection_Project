
import os
import requests
import pandas as pd
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

URL = 'https://api.abuseipdb.com/api/v2/blacklist'

# Function to fetch data
def fetch_data(api_key, min_confidence, limit):
    headers = {
        'Key': api_key,
        'Accept': 'application/json'
    }
    params = {
        'confidenceMinimum': min_confidence,
        'limit': limit
    }
    response = requests.get(URL, headers=headers, params=params)
    data = response.json()
    return data

# Fetch data for different confidence scores
data_high_confidence = fetch_data(API_KEY, 75, 10000)  # Example for high confidence
data_low_confidence = fetch_data(API_KEY, 50, 10000)   # Example for lower confidence

# Convert to DataFrame
df_high = pd.DataFrame(data_high_confidence['data'])
df_low = pd.DataFrame(data_low_confidence['data'])

# Add target column (1 for high confidence, 0 for low confidence)
df_high['target'] = 1
df_low['target'] = 0

# Combine data
df_combined = pd.concat([df_high, df_low], ignore_index=True)

# Save combined data
df_combined.to_csv('combined_abuseipdb_data.csv', index=False)

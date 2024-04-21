import json
from datetime import datetime, timedelta
import pytz 
import requests

def fetch_data(query):
    """Fetch pairs data from DeX Screener API based on a query."""
    url = f"https://api.dexscreener.com/latest/dex/search?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Return the JSON response as a dictionary
    else:
        raise Exception("Failed to fetch data from DeX Screener: HTTP Status Code", response.status_code)


# Example usage: Search for 'BASE WETH' pairs
query = "BASE WETH"
data = fetch_data(query)
print(data)

def filter_pairs(data):
    # Define the current time
    current_time = datetime.now(pytz.utc)
    
    # Define the recent pairs list
    recent_pairs = []
    
    # # Iterate over the pairs in the data
    for pair in data['pairs']:
    #     # Convert the creation timestamp from milliseconds to seconds
    #     creation_time = datetime.fromtimestamp(pair['pairCreatedAt'] / 1000, pytz.utc)
        
    #     # Calculate the time difference
    #     time_difference = current_time - creation_time

    # On SOL or BASE
    # Listed in the last 3 hours
    # Liquidity over 5 Mn > 10,000
    # Makers > 10
    # Tweetscout score > 200
        
        # Calculate total transactions in the last 5 minutes
        transactions_5m = pair['txns']['h1']['buys'] + pair['txns']['h1']['sells']
        
        # Check if the pair was created within the last 6 hours and has more than 100 transactions in the last 5 minutes
        if transactions_5m > 100:
            recent_pairs.append(pair)
    
    return recent_pairs

# Run the function
filtered_pairs = filter_pairs(data)
print(json.dumps(filtered_pairs, indent=2))
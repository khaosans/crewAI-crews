import os
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, filename='app_logs.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Check if USER_AGENT environment variable is set
user_agent = os.getenv('USER_AGENT')
if not user_agent:
    logging.warning("USER_AGENT environment variable not set, consider setting it to identify your requests.")
    user_agent = 'YourAppName/1.0 (contact@example.com)'

headers = {
    'User-Agent': user_agent,
}

def search_10q(ticker, query):
    url = f'https://data.sec.gov/submissions/CIK{ticker}.json'

    # Make the request with the User-Agent header
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # Process your data as needed
        return data
    elif response.status_code == 404:
        raise Exception(f"Error fetching data from SEC: 404 - The requested resource could not be found.")
    else:
        raise Exception(f"Error fetching data from SEC: {response.status_code}")
import requests

# Define your user agent string
headers = {
    'User-Agent': 'YourAppName/1.0 (contact@example.com)',
}

def search_10q(ticker, query):
    url = f'https://data.sec.gov/submissions/CIK{ticker}.json'

    # Make the request with the User-Agent header
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # Process your data as needed
        return data
    else:
        raise Exception(f"Error fetching data from SEC: {response.status_code}")

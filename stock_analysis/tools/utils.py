import time
import requests
import os

# Define the rate limit (e.g., 1 request per second)
RATE_LIMIT = 1  # seconds

def make_request(url, headers, payload):
    response = requests.post(url, headers=headers, data=payload)
    return response

def rate_limited_requests(url, headers, payload, num_requests):
    for _ in range(num_requests):
        response = make_request(url, headers, payload)
        print(response.status_code, response.json())
        time.sleep(RATE_LIMIT)
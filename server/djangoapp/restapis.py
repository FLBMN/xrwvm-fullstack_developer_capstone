# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="http://localhost:5050/")

# Ensure two blank lines before function definition
def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:  # Added space after if
        for key, value in kwargs.items():  # Added spaces around '='
            params = params + key + "=" + value + "&"

    request_url = backend_url + endpoint + "?" + params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as e:  # Catch specific exception
        print(f"Network exception occurred: {e}")

# Ensure two blank lines before function definition
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as e:  # Catch specific exception
        print(f"Network exception occurred: {e}")

# Ensure two blank lines before function definition
def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as e:  # Catch specific exception
        print(f"Network exception occurred: {e}")

# Add code for posting review
# Ensure two blank lines before starting new block of code


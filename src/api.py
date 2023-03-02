# requests is the package for interacting with APIs
import requests


# Function for making a request to the API address
def api_request(baseurl, endpoint):
    # The concatination of the baseurl and the endpoint is the entire request
    entire_request = requests.get(baseurl + endpoint)
    # Returns the data from the api_request
    # Without this, the api_request would return only an http client code
    return entire_request.json()

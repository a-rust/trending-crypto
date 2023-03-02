# requests is the package for interacting with APIs
import requests


# Refer to https://www.coingecko.com/en/api/documentation for complete api documentation
# The baseurl for the Coingecko api
coin_gecko_baseurl = 'https://api.coingecko.com/api/v3/'

# The search/trending endpoint gives the top 7 most searched cryptocurrencies within the last 24 hours, in order
coin_gecko_endpoint = 'search/trending'


# Function for making a request to the API address
def api_request(baseurl, endpoint):
    # The concatination of the baseurl and the endpoint is the entire request
    entire_request = requests.get(baseurl + endpoint)
    # Returns the data from the api_request
    # Without this, the api_request would return only an http client code
    return entire_request.json()


# Todo: function that puts each item in a dictionary

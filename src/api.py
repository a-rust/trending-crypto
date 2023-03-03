# requests is the package for interacting with APIs
import requests


# Function for making a request to the API address
def api_request(baseurl, endpoint):
    # The concatination of the baseurl and the endpoint is the entire request
    entire_request = requests.get(baseurl + endpoint)
    # Returns the data from the api_request
    # Without this, the api_request would return only an http client code
    return entire_request.json()


# Function that loops through the json result of the API request, and appends each cryptocurrency id to the list
def order_by_searches(entire_request):
    list = []
    for coin in entire_request['coins']:
        list.append(coin['item']['id'])
    return list


# Get the price each cryptocurrency C in terms of btc (i.e., how much btc can be bought with C)
def get_price_in_btc(entire_request):
    list = []
    for coin in entire_request['coins']:
        list.append(coin['item']['price_btc'])
    return list


# Gets the current price of btc
def get_current_btc_price():
    baseurl = 'https://api.coingecko.com/api/v3/'
    btc_endpoint = 'simple/price?ids=bitcoin&vs_currencies=usd'
    return api_request(baseurl, btc_endpoint)['bitcoin']['usd']


current_btc_price = get_current_btc_price()


# Compute usd price of each cryptocurrency C := current btc price * price of C in terms of btc
def compute_usd_price(entire_request):
    list = []
    for coin in entire_request['coins']:
        usd_price = current_btc_price * coin['item']['price_btc']
        list.append(usd_price)
    return list

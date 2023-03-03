from api import *

# Refer to https://www.coingecko.com/en/api/documentation for complete api documentation
# The baseurl for the Coingecko api
coin_gecko_baseurl = 'https://api.coingecko.com/api/v3/'

# The search/trending endpoint gives the top 7 most searched cryptocurrencies within the last 24 hours, in order
coin_gecko_endpoint = 'search/trending'


# Outputs a list of the top 7 most searched cryptocurrencies within the last 24 hours
entire_request = api_request(coin_gecko_baseurl, coin_gecko_endpoint)
list = order_by_searches(entire_request)
print(list)

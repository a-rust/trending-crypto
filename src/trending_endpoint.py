from api import *
# Refer to https://www.coingecko.com/en/api/documentation for complete api documentation
# The baseurl for the Coingecko api
coin_gecko_baseurl = 'https://api.coingecko.com/api/v3/'

# The search/trending endpoint gives the top 7 most searched cryptocurrencies within the last 24 hours, in order
coin_gecko_endpoint = 'search/trending'

# The entire API request
entire_request = api_request(coin_gecko_baseurl, coin_gecko_endpoint)

# Ordered list of the top trending cryptocurrencies
ordered_list = order_by_searches(entire_request)

# Ordered list in terms of BTC price
btc_ordered_list = get_price_in_btc(entire_request)

# Ordered list in terms of USD price
usd_ordered_list = compute_usd_price(entire_request)

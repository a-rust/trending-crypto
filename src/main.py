from argparse import ArgumentParser
from api import *

# Refer to https://www.coingecko.com/en/api/documentation for complete api documentation
# The baseurl for the Coingecko api
coin_gecko_baseurl = 'https://api.coingecko.com/api/v3/'

# The search/trending endpoint gives the top 7 most searched cryptocurrencies within the last 24 hours, in order
coin_gecko_endpoint = 'search/trending'

# The entire API request
entire_request = api_request(coin_gecko_baseurl, coin_gecko_endpoint)

parser = ArgumentParser()

# No need for positional argument, as there is just a summary of external information

# Optional argument to display the nth top trending cryptocurrency
parser.add_argument(
    '-n', '--number', help='Displays the nth top trending cryptocurrency', type=int, choices=[1, 2, 3, 4, 5, 6, 7])

# No need for verbose description

# Namespace for arguments
args = parser.parse_args()

# The ordered list of the top trending cryptocurrencies
ordered_list = order_by_searches(entire_request)

# Functionality of optional argument '-n', '--number'
for n in range(1, 7, 1):
    if args.number == n:
        print(ordered_list[n+1])

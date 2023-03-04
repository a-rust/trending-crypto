from argparse import ArgumentParser
from trending_endpoint import *


# Display the top trending data (id, btc_price, usd_pricein a nicely formatted manner
def display_full_data():
    print('--- --- --- --- ---')
    for n in range(1, 8, 1):
        print(f'Rank #{n} Top Trending Cryptocurrency on CoinGecko (ID): ' +
              str(ordered_list[n-1]))
        print(
            f'BTC Price of {str(ordered_list[n-1])}: ' + str(btc_ordered_list[n-1]))
        print(
            f'USD Price of {str(ordered_list[n-1])}: ' + str(usd_ordered_list[n-1]))
        print('--- --- --- --- ---')


parser = ArgumentParser()

# No need for positional argument, as there is just a summary of external information

# Optional argument to display the nth top trending cryptocurrency, along with BTC and USD prices
#   choices represents the query range (as there are only 7 top trending cryptocurrencies provided in the API)
#   default is a way to keep track of whether the optional argument was called or not
parser.add_argument(
    '-n', '--number', help='Displays only the nth top trending cryptocurrency', type=int, choices=[1, 2, 3, 4, 5, 6, 7], default=False)


# Namespace for arguments
args = parser.parse_args()


# Functionality of optional argument '-n', '--number'
def nth_crypto():
    for n in range(1, 8, 1):
        if args.number == n:
            print(f'Rank #{n} Top Trending Cryptocurrency on CoinGecko (ID): ' +
                  str(ordered_list[n-1]))
            print(
                f'BTC Price of {str(ordered_list[n-1])}: ' + str(btc_ordered_list[n-1]))
            print(
                f'USD Price of {str(ordered_list[n-1])}: ' + str(usd_ordered_list[n-1]))


# If the optional argument '-n' (or '--number') is not provided, then the full data containing all of the top trending cryptocurrencies will be displayed
if args.number == False:
    display_full_data()
else:
    nth_crypto()

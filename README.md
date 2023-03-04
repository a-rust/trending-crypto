# Trending Cryptocurrencies
This was an educational project for me to learn and apply ideas involving http and API requests using the requests package, and building command line tools using the argparse package. 

## Project Description
This project involved building a command line interface (CLI) tool that interacts with the API of [Coingecko.com](https://www.coingecko.com/)
  * Full documentation of Coingecko's API can be found at https://www.coingecko.com/en/api/documentation

More specifically, this CLI tool interacts with the 'search/trending' endpoint, which is a get request that returns basic information regarding the current "trending cryptocurrencies"
  * CoinGecko API defines the current trending cryptocurrencies as the 7 most searched cryptocurrencies on CoinGecko within the last 24 hours (ordered by most popular first).

**Remark**: The public API version of Coingecko (which this project utilizes) has a rate limit of 10-50 requests per hour
* This CLI tool makes just one request to access the 'search/trending' endpoint, so a single daily check using this tool shouldn't be a problem regarding the request rate limit

## Python packages used
* requests - for making requests to the CoinGecko API
* argparse - for creating the CLI tool

## Features of this CLI tool
* By default, lists the top 7 trending cryptocurrencies (ID, price in BTC, and price in USD)
* Optional argument to query the $n$th top trending cryptocurrency (returns ID, price in BTC, and price in USD)

## Example
```
$ python3 ./src/main.py -n 2
Rank #2 Top Trending Cryptocurrency on CoinGecko (ID): baby-doge-coin
BTC Price of baby-doge-coin: 1.1399609729552157e-13
USD Price of baby-doge-coin: 2.532081313128125e-09
```

## Usage
1. Clone this repo:  
```
git clone https://github.com/a-rust/trending-crypto.git  
cd trending-crypto
```
2. Enjoy! Use the help option to get a better idea of what the tool does:
```
python3 ./src/main.py -h
```








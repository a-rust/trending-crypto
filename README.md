# Trending Cryptocurrencies

## Overview 
This was an educational project for me to learn and apply ideas involving http and API requests using the requests package, and building command line tools using the argparse package. 

## Project Description
A command line interface (CLI) tool that interacts with the API of [Coingecko.com](https://www.coingecko.com/)
  * Full documentation of Coingecko's API can be found at https://www.coingecko.com/en/api/documentation

In particular, this CLI tool interacts with the API using the 'search/trending' endpoint, which returns basic information regarding the current "trending cryptocurrencies"
  * CoinGecko API defines the current trending cryptocurrencies as the 7 most searched cryptocurrencies on CoinGecko within the last 24 hours (ordered by most popular first)


# Dependencies
* Python packages:
  * requests - for making requests to the CoinGecko API
  * argparse - for creating the CLI tool

# Features
- [x] By default (no arguments), this CLI tool lists the top 7 trending cryptocurrencies (ID, price in BTC, and price in USD)
- [x] Optional argument to query for a single top trending cryptocurrency (within the top 7)

# Demo
```
python3 src/main.py -n 2
# Output:
# Rank #2 Top Trending Cryptocurrency on CoinGecko (ID): hedera-hashgraph
# BTC Price of hedera-hashgraph: 2.751284513321697e-06
# USD Price of hedera-hashgraph: 0.05585107562043045
```

# How to use
1. Clone this repo:  
```
git clone https://github.com/a-rust/trending-crypto.git  
cd trending-crypto
```
2. Enjoy! Use the help option to get a better idea of what the tool does:
```
python3 ./src/main.py -h
```

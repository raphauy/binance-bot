import ccxt
import config

# exchange= ccxt.binance()
# markets= exchange.load_markets()

#ticker= exchange.fetch_ticker('ADA/USDT')
#print(ticker)

# ohlc= exchange.fetch_ohlcvc('BTC/USDT')
# for candle in ohlc:
#     print(candle)

# for market in markets:
#     if "/BTC" in market:
#         print(market)


# exchange_id = 'binance'
# exchange_class = getattr(ccxt, exchange_id)
# exchange = exchange_class({
#     'apiKey': 'YOUR_API_KEY',
#     'secret': 'YOUR_SECRET',
# })

exchange= ccxt.binance({
    "apiKey": config.BINANCE_API_KEY,
    "secret": config.BINANCE_API_SECRET
})
balances= exchange.fetch_balance()
print(balances)
coins= ["USDT", "BNB"]
for coin in coins:
    print(coin + ": " + str(balances["total"][coin]))

import time
import ccxt
import pandas as pd

binance= ccxt.binance()
inicio = time.time()

market= binance.load_markets()
# df= pd.DataFrame(market)
# print(df)
# quote= "ADA"
# symbols= [item for item in market if item.endswith(quote)]
# aux= list(market.items())[:1]
# print(aux)

ticker= binance.fetch_ticker("BTC/USD")["last"]
print(ticker)
ticker= binance.fetch_ticker("BTC/USDT")["last"]
print(ticker)

#df= pd.DataFrame(ticker)


fin = time.time()
duracion = round(fin - inicio, 1)
print("   " + str(duracion) + "s")
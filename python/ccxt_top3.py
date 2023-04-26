import ccxt
import config
import time

binance = ccxt.binance({
    "enableRateLimit": True,
    "apiKey": config.BINANCE_API_KEY,
    "secret": config.BINANCE_API_SECRET
})

# balance= binance.fetch_balance()
# print(balance)


def get_bid_ask(pair):
    inicio = time.time()
    order_book= binance.fetch_order_book(pair)
    bids= order_book["bids"][0][0]
    asks= order_book["asks"][0][0]
    fin = time.time()
    duracion = round(fin - inicio, 1)
    print(pair + ": bids:" + str(bids)+ " - asks: " + str(asks) + f"    {duracion}s")
    return bids, asks

i= 2
while (i > 0):
    i= i-1
    #get_bid_ask("BTC/USDT")
    get_bid_ask("ADA/USDT")
    # get_bid_ask("ADA/BNB")
    # get_bid_ask("ADA/BTC")
    # get_bid_ask("BNB/BTC")
    print("------------------ " + str(i))


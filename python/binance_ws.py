import websocket
import pandas as pd
import json
import os
from ticker import Ticker, update_ticker


tickers= []
counter_adausdt= 0
counter_adabnb= 0
counter_bnbusdt= 0

def print_prices():
    os.system("clear")
    print(f"{counter_adausdt} ADAUSDT")
    print(f"{counter_adabnb} ADABNB")
    print(f"{counter_bnbusdt} BNBUSDT")
    print(f"{counter_adausdt+counter_adabnb+counter_bnbusdt} Total")
    global tickers
    for ticker in tickers:
        print(ticker)


def lets_close():    
    with open("closing.txt") as f:
        return int(f.readline()) > 0

def on_open(_wsa):
    data= dict(
        method="SUBSCRIBE",
        id=1,
        params=["adausdt@bookTicker", "adabnb@bookTicker", "bnbusdt@bookTicker"]
    )
    _wsa.send(json.dumps(data))

def on_message(_wsa, message):
    global tickers
    global counter_adausdt
    global counter_adabnb
    global counter_bnbusdt

    data= json.loads(message)
    ticker= Ticker(data)
    print(ticker.symbol + " updated!")
    update_ticker(tickers, ticker)

    if ticker.symbol == "ADAUSDT":
        counter_adausdt+= 1
    if ticker.symbol == "ADABNB":
        counter_adabnb+= 1
    if ticker.symbol == "BNBUSDT":
        counter_bnbusdt+= 1
    print_prices()

    if lets_close():
        print(f"{counter_adausdt} adausdt")
        print(f"{counter_adabnb} adabnb")
        print(f"{counter_bnbusdt} bnbusdt")
        _wsa.close()

def on_error(_wsa, error):
    print(error)


def run():
    print("running...")

    stream_name= "raphauy_binance_stream"
    wss= "wss://stream.binance.com:443/ws/%s" % stream_name
    wsa= websocket.WebSocketApp(wss, 
                                on_message=on_message,
                                on_error=on_error,
                                on_open=on_open)
    wsa.run_forever()

if __name__ == "__main__":
    run()





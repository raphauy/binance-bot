import websocket

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(close_msg):
    print(close_msg)

def streamKline(symbol, interval):
    socket= f'wss://stream.binance.com:443/ws/{symbol}@kline_{interval}'
    ws= websocket.WebSocketApp(socket, 
                               on_message=on_message,
                               on_error=on_error,
                               on_close=on_close)
    ws.run_forever()

streamKline("btcusdt", "1m")
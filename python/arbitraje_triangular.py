import json
import pytest

class Ticker:
    def __init__(self, json_data):
        self.data= json_data
        self.order_book_update_id = json_data["u"]
        self.symbol = json_data["s"]
        self.bid_price = float(json_data["b"])
        self.bid_quantity = float(json_data["B"])
        self.ask_price = float(json_data["a"])
        self.ask_quantity = float(json_data["A"])

    @property
    def price(self):
        return (self.bid_price + self.ask_price) / 2

    @property
    def spread(self):
        return self.ask_price - self.bid_price

    def __repr__(self):
        bid_price_str= "{:.8f}".format(self.bid_price)
        ask_price_str= "{:.8f}".format(self.ask_price)
        spread_str=  "{:.8f}".format(self.spread)
        return f'Ticker({self.symbol}, bid_price={bid_price_str}, ask_price={ask_price_str}, bid_Q:{self.bid_quantity}, ask_Q:{self.ask_quantity}, spread={spread_str})'

def update_ticker(tickers, ticker: Ticker):
    for i in range(len(tickers)):
        if tickers[i].symbol == ticker.symbol:
            tickers[i] = ticker
            return
    tickers.append(ticker)


class Ruta:
    def __init__(self, secuencia, profit):
        self.secuencia = secuencia
        self.profit = profit
        
    def __str__(self):
        secuencia_str = ' -> '.join(self.secuencia)
        profit_str = "{:.8f}".format(self.profit)
        return f'Ruta: {secuencia_str}, Profit: {profit_str}'

def calcular_profit(ticker1, ticker2, ticker3):
    # verificar si las tickers comparten pares de cotización
    if (ticker1.symbol[:3] in ticker2.symbol and 
#        ((ticker2.symbol[-3:] in ticker3.symbol) or (ticker2.symbol[:3] in ticker3.symbol)) and 
        ((ticker2.symbol[-3:] in ticker3.symbol) ) and 
        ticker3.symbol[-3:] in ticker1.symbol):
        # calcular los precios de oferta de cada ticker
        p1 = ticker1.ask_price / ticker2.bid_price
        p2 = ticker2.ask_price / ticker3.bid_price
        p3 = ticker3.ask_price / ticker1.bid_price

        # calcular el beneficio total
        profit = (p1 * p2 * p3) - 1

        # si el beneficio es positivo, guardar la ruta
#        if profit > 0:
        if True:
            secuencia = [ticker1.symbol, ticker2.symbol, ticker3.symbol]
            return Ruta(secuencia, profit)

    # si no hay una ruta de arbitraje, devolver None
    return None


def encontrar_rutas(tickers):
    rutas = []

    # iterar sobre todas las combinaciones de tres tickers
    for i in range(len(tickers)):
        for j in range(len(tickers)):
            for k in range(len(tickers)):
                if i != j and j != k and i != k:
                    ruta = calcular_profit(tickers[i], tickers[j], tickers[k])
                    if ruta:
                        rutas.append(ruta)

    # ordenar las rutas por beneficio descendente
    rutas.sort(key=lambda x: x.profit, reverse=True)

    return rutas

def update_ticker(tickers, ticker: Ticker):
    for i in range(len(tickers)):
        if tickers[i].symbol == ticker.symbol:
            tickers[i] = ticker
            return
    tickers.append(ticker)

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



class Ruta:
    def __init__(self, secuencia, profit, cantidad_maxima):
        self.secuencia = secuencia
        self.profit = profit
        self.cantidad_maxima = cantidad_maxima
        
    def __str__(self):
        secuencia_str = ' -> '.join(self.secuencia)
        profit_str = "{:.8f}".format(self.profit)
        cantidad_str = "{:.8f}".format(self.cantidad_maxima)
        return f'Ruta: {secuencia_str}, Profit: {profit_str}, Max.Q: {cantidad_str}'

def calcular_profit(ticker1, ticker2, ticker3):
    if ticker1.symbol[-3:] != ticker3.symbol[-3:] or ticker1.symbol[:3] != ticker2.symbol[:3] or ticker2.symbol[-3:] != ticker3.symbol[:3]:
        return None

    cantidad_intermedia1 = 1 / ticker1.ask_price
    cantidad_intermedia2 = cantidad_intermedia1 * ticker2.bid_price
    cantidad_final = cantidad_intermedia2 * ticker3.bid_price
    profit = (cantidad_final - 1) * 100
    return profit




def generar_ruta(ticker1, ticker2, ticker3, secuencia):
    if secuencia == "buy-sell-sell":
        cantidad_intermedia1 = 1 / ticker1.ask_price
        cantidad_intermedia2 = cantidad_intermedia1 * ticker2.bid_price
        cantidad_final = cantidad_intermedia2 * ticker3.bid_price
        profit = cantidad_final - 1
        cantidad_maxima = min(ticker1.ask_quantity, ticker2.bid_quantity, ticker3.bid_quantity)
    elif secuencia == "buy-sell-buy":
        cantidad_intermedia1 = 1 / ticker1.ask_price
        cantidad_final = cantidad_intermedia1 * ticker3.bid_price / ticker2.ask_price
        profit = cantidad_final - 1
        cantidad_maxima = min(ticker1.ask_quantity, ticker3.bid_quantity, ticker2.ask_quantity)
    
    ruta = Ruta(["{} {}".format(secuencia.split("-")[0], ticker1.symbol),
                 "{} {}".format(secuencia.split("-")[1], ticker2.symbol),
                 "{} {}".format(secuencia.split("-")[2], ticker3.symbol)], profit * 100, cantidad_maxima)
    return ruta


def arbitrajeTriangular(ticker1, ticker2, ticker3):
    rutas = []

    rutas.append(generar_ruta(ticker1, ticker2, ticker3, "buy-sell-sell"))
    rutas.append(generar_ruta(ticker1, ticker3, ticker2, "buy-sell-buy"))
    rutas.append(generar_ruta(ticker2, ticker1, ticker3, "buy-sell-sell"))
    rutas.append(generar_ruta(ticker2, ticker3, ticker1, "buy-sell-buy"))
    rutas.append(generar_ruta(ticker3, ticker1, ticker2, "buy-sell-sell"))
    rutas.append(generar_ruta(ticker3, ticker2, ticker1, "buy-sell-buy"))

    rutas.sort(key=lambda x: x.profit, reverse=True)

    return rutas


############################################################

# función que realiza un algoritmo de arbitraje triangular
# recibe 3 instancias de Tickers con todos sus valores
# devuelve las rutas posibles de triangulación con sus respectivos profits, proponer una clase Ruta con al información necesaria
# este es un ejemplo de input (3 instancias de Tickers):
# Ticker(ADAUSDT, bid_price=0.38100000, ask_price=0.38110000, bid_Q:720.0, ask_Q:30427.0, spread=0.00010000)
# Ticker(ADABNB, bid_price=0.00116100, ask_price=0.00116300, bid_Q:3755.8, ask_Q:3313.0, spread=0.00000200)
# Ticker(BNBUSDT, bid_price=327.80000000, ask_price=327.90000000, bid_Q:38.898, ask_Q:27.516, spread=0.10000000)
# aquí arriba podemos ver 2 markets, el market USDT y el market BNB (quote currency)
# Un ejemplo de Ruta sería: comprar ADA en el market USDT, luego vender ADA en el market BNB y por último vender BNB en el market USDT
# La ruta de arriba trae asociada el cálculo de un profit que sería la diferencia de USDT entre lo que se gastó en la primera compra y lo que se obtuvo en la última venta
# tener en cuenta las cantidades de los Tickers, la Ruta debe traer además de la secuencia de compras y ventas y de el profit, la cantidad máxima posible para esa operación
#def arbitrajeTriangular(ticker1, ticker2, ticker3):
#    return Ruta

# json_data = '{"u":7266431532,"s":"ADAUSDT","b":"0.38810000","B":"3637.80000000","a":"0.38820000","A":"20207.70000000"}'
# data = json.loads(json_data)

# ticker = Ticker(data)
# print(ticker) # Ticker(symbol=ADAUSDT, bid_price=0.3881, ask_price=0.3882, price=0.38815, spread=0.0001)



import json
import pytest
#from ticker import Ticker, Ruta, arbitrajeTriangular, generar_ruta, calcular_profit
from arbitraje_triangular import calcular_profit, encontrar_rutas, Ticker, Ruta



def test():
    json_data1 = "{'u': 7268661384, 's': 'ADAUSDT', 'b': '0.35830000', 'B': '632.10000000', 'a': '0.38840000', 'A': '108977.50000000'}"    
    data1 = json.loads(json_data1.replace("'", '"'))

    ticker1 = Ticker(data1)

    json_data2 = "{'u': 503146282, 's': 'ADABNB', 'b': '0.00217100', 'B': '770.50000000', 'a': '0.00117200', 'A': '2663.60000000'}"
    data2 = json.loads(json_data2.replace("'", '"'))
    ticker2 = Ticker(data2)

    json_data3 = "{'u': 8448273264, 's': 'BNBUSDT', 'b': '331.50000000', 'B': '181.48100000', 'a': '331.60000000', 'A': '261.94900000'}"
    data3 = json.loads(json_data3.replace("'", '"'))
    ticker3 = Ticker(data3)

#    print("Profit:", calcular_profit(ticker1, ticker2, ticker3), "%")

    rutas= encontrar_rutas([ticker1, ticker2, ticker3])
    for ruta in rutas:
        print(ruta)

test()



# rutas = arbitrajeTriangular(ticker1, ticker2, ticker3)
# for ruta in rutas:
#     print(ruta)



# rutas= encontrar_rutas([ticker1, ticker2, ticker3])
# print(rutas)

# ruta1 = generar_ruta(ticker1, ticker2, ticker3, "buy-sell-sell")
# print(ruta1)
# ruta2 = generar_ruta(ticker1, ticker3, ticker2, "buy-sell-buy")
# print(ruta2)
# ruta3 = generar_ruta(ticker2, ticker1, ticker3, "buy-sell-sell")
# print(ruta3)
# ruta4 = generar_ruta(ticker2, ticker3, ticker1, "buy-sell-buy")
# print(ruta4)
# ruta5 = generar_ruta(ticker3, ticker1, ticker2, "buy-sell-sell")
# print(ruta5)
# ruta6 = generar_ruta(ticker3, ticker2, ticker1, "buy-sell-buy")
# print(ruta6)


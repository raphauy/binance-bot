import ccxt from 'ccxt'

//var ccxt = require ('ccxt')

const binance = new ccxt.binance({ enableRateLimit: true })

let i= 0
while (i < 10) {
    var fecha_ini = new Date();
    const trades = await binance.fetchTrades('BTC/USDT:USDT')
    var fecha_fin = new Date();
    
    // Diferencia de tiempo en milisegundos
    var diferencia_tiempo = fecha_fin - fecha_ini;

    const trade = trades[0]

//    console.log(trade);
    console.log(trade.datetime.slice(11, 19) + " " + trade.amount.toFixed(3) + " btc was bought at " + trade.price.toFixed(1))
    console.log("  " + diferencia_tiempo + " ms");

    i++
}

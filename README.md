# Challenge tecnico TSS 
Este proyecto se basa en realizar una estrategia que realice compra y ventas de activos utilizando las estrategias de simple moving averages - SMA y el framework backtrader

# Requisitos
Python 2.7.18
backtrader

# Enunciado
Utilizando el framework backtrader (Welcome - Backtrader ) realizar una estrategia que realice compra y ventas de activos utilizando las siguientes estrategias de simple moving averages - SMA (How To Use a Moving Average to Buy Stocks ):

    1_  Comprar cuando el precio de un instrumento supere a una SMA de 10 velas diarias y vender cuando el precio caiga por debajo de la misma.

    2_  Comprar cuando el precio de un instrumento supere a una SMA de 30 velas diarias y vender cuando el precio caiga por debajo de la misma.

    3_  Utilizando una SMA de 10 velas diarias y otra de 30 velas diarias, comprar cuando la vela de 10 cruce sobre la vela de 30 superandola y vender cuando la vela de 30 cruce sobre la vela de 10 superandola (Golden Cross Pattern Explained With Examples and Charts ). 

Importante: solo se podrá vender un activo utilizando la misma estrategia que se utilizó para comprarlo. 

En caso de que se active una venta de un instrumento en el cual ya se está comprado, se podrá comprar más pero se deberá tener registro de cuánto se compró con cada estrategia.

Para cada compra se destinará el 10% del valor total de la cartera al momento en que se genera la señal de compra. En caso de no contar con liquidez para la misma, no se realizará la compra. 

Se deberán utilizar los siguientes instrumentos para el periodo del año 2021 los cuales podrán ser obtenidos utilizando el data feeder de backtrader de YahooFinanceData (Data Feeds - Yahoo - Backtrader ):

    _MFST

    _GOOG

    _APPL

    _TSLA 

Otras consideraciones:

Suponer 100000 usd de capital inicial.

No se puede vender algo que no se tiene

Output: Se deberá generar un listado de todas las transacciones realizadas durante el periodo analizado como así también las variaciones del valor del portfolio incluido su valor final.
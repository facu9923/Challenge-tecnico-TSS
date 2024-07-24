# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
import inicData as inicData
import Move_pyc as Move_pyc
import csv
from Strategies.data1Strategy import data1Strategy
from Strategies.data2Strategy import data2Strategy
from Strategies.data3Strategy import data3Strategy
from Strategies.data4Strategy import data4Strategy

def main():

    cerebro = bt.Cerebro()

    cerebro.broker.setcash(100000)
    cerebro.broker.setcommission(commission=0.001)

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    inicData.addData(cerebro)

    cerebro.addstrategy(data1Strategy)
    cerebro.addstrategy(data2Strategy)
    cerebro.addstrategy(data3Strategy)
    cerebro.addstrategy(data4Strategy)

    filename = 'transactions.csv'

    with open(filename, 'w') as csvfile:
        csvfile.write('Lista de ordenes de compra y venta de los instrumentos GOOG, AAPL, MSFT y TSLA\n\n')
        fieldnames = ['activo', 'tipo', 'precio', 'cantidad', 'fecha(dd-mm-aaaa)', 'portafolio value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

    cerebro.run()

    # Se imprimern 4 graficos, cada describe la estrategia de cada instrumento
    # Se comenta la linea para que no se muestren los graficos 
    # a

    # cerebro.plot()

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    print('Transactions saved in transactions.csv')

    Move_pyc.mover_pyc_a_directorio('pyc_files')
if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
import inicData as inicData
import Move_pyc as Move_pyc
from Strategies.Sma10 import StrategySMA10 
from Strategies.Sma30 import StrategySMA30 
from Strategies.StrategyCrossover import StrategyCrossover 

def main():

    cerebro = bt.Cerebro()

    cerebro.broker.setcash(100000)
    cerebro.broker.setcommission(commission=0.001)

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    inicData.addData(cerebro)

    cerebro.addstrategy(StrategySMA10)
    cerebro.addstrategy(StrategySMA30)
    cerebro.addstrategy(StrategyCrossover)

    cerebro.run()

    # cerebro.plot()

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    transactions = []


    Move_pyc.mover_pyc_a_directorio('pyc_files')
if __name__ == '__main__':
    main()

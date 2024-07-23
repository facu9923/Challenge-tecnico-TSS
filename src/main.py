# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
import inicData as inicData
import Move_pyc as Move_pyc
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

    # cerebro.addstrategy(data1Strategy)
    # cerebro.addstrategy(data2Strategy)
    cerebro.addstrategy(data3Strategy)
    # cerebro.addstrategy(data4Strategy)

    cerebro.run()

    # cerebro.plot()
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    Move_pyc.mover_pyc_a_directorio('pyc_files')
if __name__ == '__main__':
    main()

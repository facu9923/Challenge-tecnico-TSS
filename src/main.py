from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
from Strategy import MyStrategy
import inicData
import Move_pyc

def main():

    cerebro = bt.Cerebro()

    cerebro.broker.setcash(100000)
    cerebro.broker.setcommission(commission=0.001)

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    inicData.addData(cerebro)

    cerebro.addstrategy(MyStrategy)

    cerebro.run()

    cerebro.plot()

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

if __name__ == '__main__':
    main()
    Move_pyc.mover_pyc_a_directorio('pyc_files')
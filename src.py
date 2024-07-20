from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
import datetime
import os
import sys

class MyStrategy(bt.Strategy):
    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(
            self.data, period=10, plotname="10 SMA"
        )
        self.sma = bt.indicators.SimpleMovingAverage(
            self.data, period=30 , plotname="30 SMA"
        )

    def next(self):
        if self.sma > self.data.close:
            # Do something
            pass

        elif self.sma < self.data.close:
            # Do something else
            pass

def addData(cerebro):

    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))

    datapathGOOG = os.path.join(modpath, './data/GOOG.csv')
    datapathAAPL = os.path.join(modpath, './data/AAPL.csv')
    datapathMSFT = os.path.join(modpath, './data/MSFT.csv')
    datapathTSLA = os.path.join(modpath, './data/TSLA.csv')

    data1 = bt.feeds.YahooFinanceCSVData(
        dataname=datapathGOOG,
        reverse=False
    )

    data2 = bt.feeds.YahooFinanceCSVData(
        dataname=datapathAAPL,
        reverse=False
    )

    data3 = bt.feeds.YahooFinanceCSVData(
        dataname=datapathMSFT,
        reverse=False
    )

    data4 = bt.feeds.YahooFinanceCSVData(
        dataname=datapathTSLA,
        reverse=False
    )
    
    cerebro.adddata(data1)

    data2.compensate(data1)
    data2.plotinfo.plotmaster = data1
    data2.plotinfo.sameaxis = True 
    cerebro.adddata(data2)

    data3.compensate(data1)
    data3.plotinfo.plotmaster = data1
    data3.plotinfo.sameaxis = True 

    cerebro.adddata(data3)

    data4.compensate(data1)
    data4.plotinfo.plotmaster = data1
    data4.plotinfo.sameaxis = True 

    cerebro.adddata(data4)

def main():

    cerebro = bt.Cerebro()

    cerebro.broker.setcash(100000)
    cerebro.broker.setcommission(commission=0.001)

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    addData(cerebro)

    cerebro.addstrategy(MyStrategy)

    cerebro.run()

    cerebro.plot()
    

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

if __name__ == '__main__':
    main()
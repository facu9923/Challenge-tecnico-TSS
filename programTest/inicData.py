import datetime
import os
import sys
import backtrader as bt

def addData(cerebro):

    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))

    datapathGOOG = os.path.join(modpath, '../data/GOOG.csv')
    datapathAAPL = os.path.join(modpath, '../data/AAPL.csv')
    datapathMSFT = os.path.join(modpath, '../data/MSFT.csv')
    datapathTSLA = os.path.join(modpath, '../data/TSLA.csv')

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
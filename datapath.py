import backtrader as bt
import os
import sys

modpath = os.path.dirname(os.path.abspath(sys.argv[0]))

datapath = os.path.join(modpath, './data/GOOG.csv')

data = bt.feeds.YahooFinanceCSVData(
    dataname=datapath,
    reverse=False
)

print(data)
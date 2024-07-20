data1 = bt.feeds.YahooFinanceCSVData(
    dataname='GOOG.csv',
    fromdate=datetime.datetime(2021, 1, 1),
    todate=datetime.datetime(2021, 12, 31),
)

data2 = bt.feeds.YahooFinanceCSVData(
    dataname='AAPL.csv',
    fromdate=datetime.datetime(2021, 1, 1),
    todate=datetime.datetime(2021, 12, 31),
)

data3 = bt.feeds.YahooFinanceCSVData(
    dataname='TSLA.csv',
    fromdate=datetime.datetime(2021, 1, 1),
    todate=datetime.datetime(2021, 12, 31),
)

data4 = bt.feeds.YahooFinanceCSVData(
    dataname='MSFT.csv',
    fromdate=datetime.datetime(2021, 1, 1),
    todate=datetime.datetime(2021, 12, 31),
)

import backtrader as bt

class MyStrategy(bt.Strategy):
    def __init__(self):

        ## indicadores para data1 (GOOG)
        self.sma_data1_10 = bt.indicators.SimpleMovingAverage(
            self.datas[0], period=10, plotname="10 SMA_1"
        )
        self.sma_data1_30 = bt.indicators.SimpleMovingAverage(
            self.datas[0], period=30 , plotname="30 SMA_1"
        )

        ## indicadores para data2 (AAPL)
        self.sma_data2_10 = bt.indicators.SimpleMovingAverage(
            self.datas[1], period=10, plotname="10 SMA_2"
        )
        self.sma_data2_30 = bt.indicators.SimpleMovingAverage(
            self.datas[1], period=30 , plotname="30 SMA_2"
        )

        ## indicadores para data3 (MSFT)
        self.sma_data3_10 = bt.indicators.SimpleMovingAverage(
            self.datas[2], period=10, plotname="10 SMA_3"
        )
        self.sma_data3_30 = bt.indicators.SimpleMovingAverage(
            self.datas[2], period=30 , plotname="30 SMA_3"
        )

        ## indicadores para data4 (TSLA)
        self.sma_data4_10 = bt.indicators.SimpleMovingAverage(
            self.datas[3], period=10, plotname="10 SMA_4"
        )
        self.sma_data4_30 = bt.indicators.SimpleMovingAverage(
            self.datas[3], period=30 , plotname="30 SMA_4"
        )

    def next(self):
        if self.sma_data1_10 > self.datas[0].close:
            self.sell()
            pass

        elif self.sma_data1_10 < self.datas[0].close:
            self.buy()
            pass

        if self.sma_data1_30 > self.datas[0].close:
            self.sell()
            pass

        elif self.sma_data1_30 < self.datas[0].close:
            self.buy()
            pass

        if self.sma_data1_10 > self.sma_data1_30:
            self.buy()
            pass
        
        elif self.sma_data1_30 < self.sma_data1_30:
            self.sell()
            pass
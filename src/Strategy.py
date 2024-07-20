import backtrader as bt

class MyStrategy(bt.Strategy):
    def __init__(self):
        self.sma10 = bt.indicators.SimpleMovingAverage(
            self.data, period=10, plotname="10 SMA"
        )
        self.sma30 = bt.indicators.SimpleMovingAverage(
            self.data, period=30 , plotname="30 SMA"
        )

    def next(self):
        if self.sma10 > self.data.close:
            self.sell()
            pass

        elif self.sma10 < self.data.close:
            self.buy()
            pass

        if self.sma30 > self.data.close:
            self.sell()
            pass

        elif self.sma30 < self.data.close:
            self.buy()
            pass

        if self.sma10 > self.sma30:
            self.buy()
            pass
        
        elif self.sma10 < self.sma30:
            self.sell()
            pass
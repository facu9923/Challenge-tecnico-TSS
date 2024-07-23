import backtrader as bt
from datetime import datetime

class MyStrategy(bt.Strategy):
    def __init__(self):
        self.sma0 = bt.indicators.SimpleMovingAverage(self.data0, period=15)
        self.sma1 = bt.indicators.SimpleMovingAverage(self.data1, period=15)

    def next(self):
        # Posición en data0
        position0 = self.getposition(self.data0)
        print(f'Data0: {self.data0._name}, Position Size: {position0.size}')

        # Comprar en data0 si no tenemos posición y el cierre está por encima de SMA
        if not position0:
            if self.data0.close[0] > self.sma0[0]:
                print(f'Comprar en data0: {self.data0._name}')
                self.buy(data=self.data0, size=100)
        # Vender en data0 si tenemos posición y el cierre está por debajo de SMA
        elif self.data0.close[0] < self.sma0[0]:
            print(f'Vender en data0: {self.data0._name}')
            self.sell(data=self.data0, size=100)

        # Posición en data1
        position1 = self.getposition(self.data1)
        print(f'Data1: {self.data1._name}, Position Size: {position1.size}')

        # Comprar en data1 si no tenemos posición y el cierre está por encima de SMA
        if not position1:
            if self.data1.close[0] > self.sma1[0]:
                print(f'Comprar en data1: {self.data1._name}')
                self.buy(data=self.data1, size=100)
        # Vender en data1 si tenemos posición y el cierre está por debajo de SMA
        elif self.data1.close[0] < self.sma1[0]:
            print(f'Vender en data1: {self.data1._name}')
            self.sell(data=self.data1, size=100)

if __name__ == '__main__':
    cerebro = bt.Cerebro()
    cerebro.addstrategy(MyStrategy)

    # Agregar el primer conjunto de datos
    data0 = bt.feeds.YahooFinanceData(dataname='AAPL', fromdate=datetime(2020, 1, 1), todate=datetime(2021, 1, 10))
    data0._name = 'AAPL'
    cerebro.adddata(data0)

    # Agregar el segundo conjunto de datos
    data1 = bt.feeds.YahooFinanceData(dataname='MSFT', fromdate=datetime(2020, 1, 1), todate=datetime(2021, 1, 10))
    data1._name = 'MSFT'
    cerebro.adddata(data1)

    cerebro.run()
    cerebro.plot()
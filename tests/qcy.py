import backtrader as bt
import datetime

# Clase base para las estrategias que lleva el registro de las compras
class BaseStrategy(bt.Strategy):
    def __init__(self):
        self.buy_records = {}  # Diccionario para registrar qué estrategia compró qué data

    def notify_order(self, order):
        if order.status in [order.Completed]:
            if order.isbuy():
                self.buy_records[order.data] = order.info['strategy_id']
            elif order.issell():
                if self.buy_records.get(order.data) == order.info['strategy_id']:
                    del self.buy_records[order.data]

class StrategySMA10(BaseStrategy):
    strategy_id = 'sma10'
    
    def __init__(self):
        BaseStrategy.__init__(self)
        self.sma10 = [bt.indicators.SimpleMovingAverage(data, period=10) for data in self.datas]

    def next(self):
        portfolio_value = self.broker.getvalue()
        cash_to_spend = portfolio_value * 0.10

        for i, data in enumerate(self.datas):
            price = data.close[0]
            position = self.getposition(data)

            if price > self.sma10[i][0] and not position:
                size = cash_to_spend / price
                self.buy(data=data, size=size, info={'strategy_id': self.strategy_id})
            elif price < self.sma10[i][0] and position.size > 0:
                if self.buy_records.get(data) == self.strategy_id:
                    self.sell(data=data, size=position.size, info={'strategy_id': self.strategy_id})

class StrategySMA30(BaseStrategy):
    strategy_id = 'sma30'
    
    def __init__(self):
        BaseStrategy.__init__(self)
        self.sma30 = [bt.indicators.SimpleMovingAverage(data, period=30) for data in self.datas]

    def next(self):
        portfolio_value = self.broker.getvalue()
        cash_to_spend = portfolio_value * 0.10

        for i, data in enumerate(self.datas):
            price = data.close[0]
            position = self.getposition(data)

            if price > self.sma30[i][0] and not position:
                size = cash_to_spend / price
                self.buy(data=data, size=size, info={'strategy_id': self.strategy_id})
            elif price < self.sma30[i][0] and position.size > 0:
                if self.buy_records.get(data) == self.strategy_id:
                    self.sell(data=data, size=position.size, info={'strategy_id': self.strategy_id})

class StrategyCrossover(BaseStrategy):
    strategy_id = 'crossover'
    
    def __init__(self):
        BaseStrategy.__init__(self)
        self.sma10 = [bt.indicators.SimpleMovingAverage(data, period=10) for data in self.datas]
        self.sma30 = [bt.indicators.SimpleMovingAverage(data, period=30) for data in self.datas]
        self.crossover = [bt.indicators.CrossOver(self.sma10[i], self.sma30[i]) for i, data in enumerate(self.datas)]

    def next(self):
        portfolio_value = self.broker.getvalue()
        cash_to_spend = portfolio_value * 0.10

        for i, data in enumerate(self.datas):
            price = data.close[0]
            position = self.getposition(data)

            if self.crossover[i] > 0 and not position:
                size = cash_to_spend / price
                self.buy(data=data, size=size, info={'strategy_id': self.strategy_id})
            elif self.crossover[i] < 0 and position.size > 0:
                if self.buy_records.get(data) == self.strategy_id:
                    self.sell(data=data, size=position.size, info={'strategy_id': self.strategy_id})

# Configuración del cerebro y adición de datas
cerebro = bt.Cerebro()
cerebro.addstrategy(StrategySMA10)
cerebro.addstrategy(StrategySMA30)
cerebro.addstrategy(StrategyCrossover)

# Cargar datos de Yahoo Finance
tickers = ['MSFT', 'GOOG', 'AAPL', 'TSLA']
for ticker in tickers:
    data = bt.feeds.YahooFinanceData(
        dataname=ticker,
        fromdate=datetime.datetime(2021, 1, 1),
        todate=datetime.datetime(2021, 12, 31)
    )
    cerebro.adddata(data)

# Establecer el capital inicial
cerebro.broker.set_cash(100000)

# Ejecutar la estrategia
cerebro.run()

# Imprimir el valor final de la cartera
print 'Valor final de la cartera: %.2f' % cerebro.broker.getvalue()

# Guardar las transacciones y el valor del portafolio en un archivo
transactions = []
for strat in cerebro.strats:
    for order in strat[0].orders:
        transactions.append([order.data._name, order.info['strategy_id'], order.executed.price, order.executed.size, order.executed.value])

with open("transactions.csv", "w") as f:
    f.write("Ticker,Estrategia,Precio,Tamaño,Valor\n")
    for t in transactions:
        f.write("{},{},{},{},{}\n".format(*t))

print "Las transacciones se han guardado en transactions.csv"
import backtrader as bt
import csv

class data4Strategy(bt.Strategy):  
    def __init__(self):
        self.sma10 = bt.indicators.SimpleMovingAverage(self.datas[3], period=10, plotname="10 SMA_1")
        self.sma30 = bt.indicators.SimpleMovingAverage(self.datas[3], period=30, plotname="30 SMA_1")
        self.crossover = bt.indicators.CrossOver(self.sma10, self.sma30)

        self.buy_records = [] 

    def notify_order(self, order):
        filename = 'transactions.csv'
        def add_transaction(activo, tipo, precio, cantidad, fecha):
            with open(filename, 'a') as csvfile:
                fieldnames = ['activo', 'tipo', 'precio', 'cantidad', 'fecha']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({
                    'activo': activo,
                    'tipo': tipo,
                    'precio': precio,
                    'cantidad': cantidad,
                    'fecha': fecha
                })

        if order.status in [order.Completed]:
            if order.isbuy():
                self.getposition(self.data3).size = self.getposition(self.data3).size + order.executed.size
                self.getposition(self.data0).size -= order.executed.size
                add_transaction(order.data._name, 'BUY', order.executed.price, order.executed.size, order.executed.dt)
                info = order.info['info'].pop()
                self.buy_records.append({'clave': {order.executed.size}, 'atributo': {info}})
            elif order.issell(): 
                self.getposition(self.data3).size = self.getposition(self.data3).size + order.executed.size
                self.getposition(self.data0).size = self.getposition(self.data0).size - order.executed.size
                add_transaction(order.data._name, 'SELL', order.executed.price, order.executed.size, order.executed.dt)


    def next(self):

        # logica de data 4

        portfolio_value = self.broker.getvalue()
        cash_to_spend = portfolio_value * 0.10
        price = self.datas[3].close[0]
        size1 = cash_to_spend / price
        position = self.getposition(self.datas[3])

        # logica de sma10
        strategy_id_sma10 = 'sma10'
        if price > self.sma10[0]:
            if int(size1) > 0:
                self.buy(data=self.datas[3], size=int(size1), info={strategy_id_sma10})
        elif price < self.sma10[0] and int(position.size) > 0:
            for elemento in self.buy_records:
                if elemento['atributo'] == {strategy_id_sma10}:
                    self.sell(data=self.datas[3], size=int(elemento['clave'].pop()), info={strategy_id_sma10})
                    self.buy_records.remove(elemento)

        # logica de sma30
        strategy_id_sma30 = 'sma30'
        if price > self.sma30[0]:
            if size1 > 0:
                self.buy(data=self.datas[3], size=int(size1), info={strategy_id_sma30})
        elif price < self.sma30[0] and int(position.size) > 0:
            for elemento in self.buy_records:
                if elemento['atributo'] == {strategy_id_sma30}: 
                    self.sell(data=self.datas[3], size=int(elemento['clave'].pop()), info={strategy_id_sma30})
                    self.buy_records.remove(elemento)

        # logica de crossover
        strategy_id_crossover = 'crossover'
        if self.crossover > 0:
           if size1 > 0:
                self.buy(data=self.datas[3], size=int(size1), info={strategy_id_crossover})
        elif self.crossover < 0 and int(position.size) > 0:
            for elemento in self.buy_records:
                if elemento['atributo'] == {strategy_id_crossover}:
                    self.sell(data=self.datas[3], size=int(elemento['clave'].pop()), info={strategy_id_crossover})
                    self.buy_records.remove(elemento) 
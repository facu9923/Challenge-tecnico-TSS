import backtrader as bt
import ListofData as ListofData

class data2Strategy(bt.Strategy):  
    def __init__(self):
        self.sma10 = bt.indicators.SimpleMovingAverage(self.datas[1], period=10, plotname="10 SMA_1")
        self.sma30 = bt.indicators.SimpleMovingAverage(self.datas[1], period=30, plotname="30 SMA_1")
        self.crossover = bt.indicators.CrossOver(self.sma10, self.sma30)

        self.buy_records = [] 

    def notify_order(self, order):
        a = self.getposition(self.datas[0])
        if order.status in [order.Completed]:
            if order.isbuy():
                print('BUY EXECUTED, Price: %.2f, Cost: %.2f, size %.2f' % (order.executed.price, order.executed.value, order.executed.size))
                self.getposition(self.data1).size = self.getposition(self.data1).size + order.executed.size
                self.getposition(self.data0).size -= order.executed.size
                print('position de data comprada', self.getposition(self.datas[1]).size)
                
                info = order.info['info'].pop()
                self.buy_records.append({'clave': {order.executed.size}, 'atributo': {info}})
            elif order.issell(): 
                pass
                print('SELL EXECUTED, Price: %.2f, Cost: %.2f, size %.2f' % (order.executed.price, order.executed.value, order.executed.size))
                # # info = order.info['info'].pop()
                # # print({'clave': order.data._name, 'atributo': info, })
                self.getposition(self.data1).size = self.getposition(self.data1).size + order.executed.size
                self.getposition(self.data0).size = self.getposition(self.data0).size - order.executed.size
                print('position de data vendida', self.getposition(self.datas[1]).size)
               

    def next(self):

        portfolio_value = self.broker.getvalue()
        cash_to_spend = portfolio_value * 0.10
        
        # logic data 2
        price = self.datas[1].close[0]
        position = self.getposition(self.data1)
        print('position de data 2 sin na', self.getposition(self.datas[1]).size)
        strategy_id_sma10 = 'sma10'
        if price > self.sma10[0]:
            size1 = cash_to_spend / price
            if size1 > 0:
                self.buy(data=self.data1, size=size1, info={strategy_id_sma10})
        elif price < self.sma10[0] and position.size > 0:
            for elemento in self.buy_records:
                if elemento['atributo'] == {strategy_id_sma10}:
                    self.sell(data=self.data1, size = elemento['clave'].pop(), info={strategy_id_sma10})
                    self.buy_records.remove(elemento) 
        
        strategy_id_sma30 = 'sma30'
        if price > self.sma30[0]:
            size1 = cash_to_spend / price
            if size1 > 0:
                self.buy(data=self.data1, size=size1, info={strategy_id_sma30})
        elif price < self.sma30[0] and position.size > 0:
            for elemento in self.buy_records:
                if elemento['atributo'] == {strategy_id_sma30}:
                    self.sell(data=self.data1, size = elemento['clave'].pop(), info={strategy_id_sma30})
                    self.buy_records.remove(elemento) 

        strategy_id_crossover = 'crossover'
        if self.crossover > 0 and not position:
            size1 = cash_to_spend / price
            self.buy(data=self.data1, size=size1, info={strategy_id_crossover})
        elif self.crossover < 0 and position.size > 0:
            for elemento in self.buy_records:
                if elemento['atributo'] == {strategy_id_crossover}:
                    self.sell(data=self.data1, size = elemento['clave'].pop(), info={strategy_id_crossover})
                    self.buy_records.remove(elemento) 
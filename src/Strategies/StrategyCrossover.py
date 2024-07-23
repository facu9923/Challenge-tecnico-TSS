# import backtrader as bt
# import orders

# class StrategyCrossover(bt.Strategy):
#     strategy_id = 'crossover'
    
#     def __init__(self):
#         # BaseStrategy(StrategyCrossover, self).__init__()

#         # INIT INDICATORS DATA 1
#         self.sma_data1_10 = bt.indicators.SimpleMovingAverage(
#             self.datas[0], period=10, plotname="10 SMA_1"
#         )
#         self.sma_data1_30 = bt.indicators.SimpleMovingAverage(
#             self.datas[0], period=30, plotname="30 SMA_1"
#         )
#         self.crossover_data1 = bt.indicators.CrossOver(self.sma_data1_10, self.sma_data1_30)

#         # INIT INDICATORS DATA 2
#         self.sma_data2_10 = bt.indicators.SimpleMovingAverage(
#             self.datas[1], period=10, plotname="10 SMA_2"
#         )
#         self.sma_data2_30 = bt.indicators.SimpleMovingAverage(
#             self.datas[1], period=30, plotname="30 SMA_2"
#         )
#         self.crossover_data2 = bt.indicators.CrossOver(self.sma_data2_10, self.sma_data2_30)

#         #INIT INDICATORS DATA 3

#         self.sma_data3_10 = bt.indicators.SimpleMovingAverage(
#             self.datas[2], period=10, plotname="10 SMA_3"
#         )
#         self.sma_data3_30 = bt.indicators.SimpleMovingAverage(
#             self.datas[2], period=30, plotname="30 SMA_3"
#         )
#         self.crossover_data3 = bt.indicators.CrossOver(self.sma_data3_10, self.sma_data3_30)

#         #INIT INDICATORS DATA 4

#         self.sma_data4_10 = bt.indicators.SimpleMovingAverage(
#             self.datas[3], period=10, plotname="10 SMA_4"
#         )
#         self.sma_data4_30 = bt.indicators.SimpleMovingAverage(
#             self.datas[3], period=30, plotname="30 SMA_4"
#         )
#         self.crossover_data4 = bt.indicators.CrossOver(self.sma_data4_10, self.sma_data4_30)

#     def next(self):
#         price1 = self.datas[0].close[0]
#         price2 = self.datas[1].close[0]
#         price3 = self.datas[2].close[0]
#         price4 = self.datas[3].close[0]


#         if self.crossover_data1 > 0 :
#             orders.buy(self, self.datas[0], price1, info={'strategy_id': self.strategy_id})
#         elif self.crossover_data1 < 0:
#             orders.sell(self, self.datas[0], info={'strategy_id': self.strategy_id})

#         if self.crossover_data2 > 0 :
#             orders.buy(self, self.datas[1], price2, info={'strategy_id': self.strategy_id})
#         elif self.crossover_data2 < 0:
#             orders.sell(self, self.datas[1], info={'strategy_id': self.strategy_id})
    
        # if self.crossover_data3 > 0 :
        #     orders.buy(self, self.datas[2], price3, info={'strategy_id': self.strategy_id})
        # elif self.crossover_data3 < 0:
        #     orders.sell(self, self.datas[2], info={'strategy_id': self.strategy_id})

        # if self.crossover_data4 > 0 :
        #     orders.buy(self, self.datas[3], price4, info={'strategy_id': self.strategy_id})
        # elif self.crossover_data4 < 0:
        #     orders.sell(self, self.datas[3], info={'strategy_id': self.strategy_id})

import backtrader as bt
from tests.BaseStrategy import BaseStrategy

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
import backtrader as bt
from BaseStrategy import BaseStrategy
# import orders

# class StrategySMA10(bt.Strategy):
#     strategy_id = 'sma10'
    
#     def __init__(self):
#         # BaseStrategy(StrategySMA10, self).__init__()

#         self.sma_data1_10 = bt.indicators.SimpleMovingAverage(
#             self.datas[0], period=10, plotname="10 SMA_1"
#         )

#         self.sma_data2_10 = bt.indicators.SimpleMovingAverage(
#             self.datas[1], period=10, plotname="10 SMA_2"
#         )

#         self.sma_data3_10 = bt.indicators.SimpleMovingAverage(
#             self.datas[2], period=10, plotname="10 SMA_3"
#         )

#         self.sma_data4_10 = bt.indicators.SimpleMovingAverage(
#             self.datas[3], period=10, plotname="10 SMA_4"
#         )

#     def next(self):
#         price1 = self.datas[0].close[0]
#         price2 = self.datas[1].close[0]
#         price3 = self.datas[2].close[0]
#         price4 = self.datas[3].close[0]

#         if self.sma_data1_10 > self.datas[0].close:
#             orders.sell(self, self.datas[0], info={'strategy_id': self.strategy_id})
#         elif self.sma_data1_10 < self.datas[0].close:
#             orders.buy(self, self.datas[0], price1, info={'strategy_id': self.strategy_id})

#         if self.sma_data2_10 > self.datas[1].close:
#             orders.sell(self, self.datas[1], info={'strategy_id': self.strategy_id})
#         elif self.sma_data2_10 < self.datas[1].close:
#             orders.buy(self, self.datas[1], price2, info={'strategy_id': self.strategy_id})

#         if self.sma_data3_10 > self.datas[2].close:
#             orders.sell(self, self.datas[2], info={'strategy_id': self.strategy_id})
#         elif self.sma_data3_10 < self.datas[2].close:
#             orders.buy(self, self.datas[2], price3, info={'strategy_id': self.strategy_id})

#         if self.sma_data4_10 > self.datas[3].close:
#             orders.sell(self, self.datas[3], info={'strategy_id': self.strategy_id})
#         elif self.sma_data4_10 < self.datas[3].close:
#             orders.buy(self, self.datas[3], price4, info={'strategy_id': self.strategy_id})



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

            if price > self.sma10[i][0] :
                size = cash_to_spend / price
                self.buy(data=data, size=size, info={'strategy_id': self.strategy_id})
            elif price < self.sma10[i][0] and position.size > 0:
                if self.buy_records.get(data) == self.strategy_id:
                    self.sell(data=data, size=position.size, info={'strategy_id': self.strategy_id})
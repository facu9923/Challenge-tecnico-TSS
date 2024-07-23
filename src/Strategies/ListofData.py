import backtrader as bt

class ListofData(bt.Strategy):
    def __init__(self):
        self.listOrders = []
    
    # def stop(self):
    #     for i in self.listOrders:
    #         print(i)
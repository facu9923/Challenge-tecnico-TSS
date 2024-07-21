def buy(self, data, price):
    portafolio_value = self.broker.getvalue()
    cash_to_spend = portafolio_value * 0.1
    size = cash_to_spend / price
    self.buy(data, size=size)

def sell(self, data):
    position = self.getposition(data)
    if position.size > 0:
        self.sell(data=data)

def logic_data1(self):

    price = self.datas[0].close[0]

    if self.sma_data1_10 > self.datas[0].close:
        sell(self, self.datas[0])
        pass

    elif self.sma_data1_10 < self.datas[0].close:
        buy(self, self.datas[0], price)
        pass

    if self.sma_data1_30 > self.datas[0].close:
        sell(self, self.datas[0])
        pass

    elif self.sma_data1_30 < self.datas[0].close:
        buy(self, self.datas[0], price)
        pass

    if self.crossover_data1 > 0 :
        buy(self, self.datas[0], price)
        pass
    elif self.crossover_data1 < 0:
        sell(self, self.datas[0])
        pass


def logic_data2(self):

    price = self.datas[1].close[0]

    if self.sma_data2_10 > self.datas[1].close:
        sell(self, self.datas[1])
        pass

    elif self.sma_data2_10 < self.datas[1].close:
        buy(self, self.datas[1], price)
        pass

    if self.sma_data2_30 > self.datas[1].close:
        sell(self, self.datas[1])
        pass

    elif self.sma_data2_30 < self.datas[1].close:
        buy(self, self.datas[1], price)
        pass

    if self.crossover_data2 > 0 :
        buy(self, self.datas[1], price)
        pass
    elif self.crossover_data2 < 0:
        sell(self, self.datas[1])
        pass

def logic_data3(self):

    price = self.datas[2].close[0]

    if self.sma_data3_10 > self.datas[2].close:
        sell(self, self.datas[2])
        pass

    elif self.sma_data3_10 < self.datas[2].close:
        buy(self, self.datas[2], price)
        pass

    if self.sma_data3_30 > self.datas[2].close:
        sell(self, self.datas[2])
        pass

    elif self.sma_data3_30 < self.datas[2].close:
        buy(self, self.datas[2], price)
        pass

    if self.crossover_data3 > 0 :
        buy(self, self.datas[2], price)
        pass
    elif self.crossover_data3 < 0:
        sell(self, self.datas[2])
        pass

def logic_data4(self):

    price = self.datas[3].close[0]

    if self.sma_data4_10 > self.datas[3].close:
        sell(self, self.datas[3])
        pass

    elif self.sma_data4_10 < self.datas[3].close:
        buy(self, self.datas[3], price)
        pass

    if self.sma_data4_30 > self.datas[3].close:
        sell(self, self.datas[3])
        pass

    elif self.sma_data4_30 < self.datas[3].close:
        buy(self, self.datas[3], price)
        pass

    if self.crossover_data4 > 0 :
        buy(self, self.datas[3], price)
        pass
    elif self.crossover_data4 < 0:
        sell(self, self.datas[3])
        pass
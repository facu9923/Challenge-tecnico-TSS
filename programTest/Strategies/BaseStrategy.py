# -*- coding: utf-8 -*-
import backtrader as bt

class BaseStrategy(bt.Strategy):
    def __init__(self):
        self.buy_records = {} 
        self.buy_orders = []  # Lista para almacenar órdenes de compra
        self.sell_orders = []  # Lista para almacenar órdenes de venta

    def notify_order(self, order):
        if order.status in [order.Completed]:
            if order.isbuy():
                self.buy_records[order.data] = order.info['strategy_id']
                self.buy_orders.append(order) 
            else:
                self.sell_orders.append(order) 
                if self.buy_records.get(order.data) == order.info['strategy_id']:
                    del self.buy_records[order.data]


    def stop(self):
        # Al final de la estrategia, imprime todas las órdenes
        print("Órdenes de Compra Completadas:")
        for order in self.buy_orders:
            print(order.data._name, order.executed.price)

        print("Órdenes de Venta Completadas:")
        for order in self.sell_orders:
            print(order.data._name, order.executed.price)
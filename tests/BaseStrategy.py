# -*- coding: utf-8 -*-
import backtrader as bt

class BaseStrategy(bt.Strategy):
    def __init__(self):
        self.buy_records = []  
        self.buy_orders = []  # Lista para almacenar órdenes de compra
        self.sell_orders = []  # Lista para almacenar órdenes de venta

    def notify_order(self, order):

        if order.status in [order.Completed]:
            if order.isbuy():
                print("SE INTENTA COMPRAR", order.data._name, order.info['info'])
                self.buy_records.append({'clave': order.data._name, 'atributo': order.info['info']})
                self.buy_orders.append(order) 
            else:
                print("SE INTENTA ELIMINAR", order.data._name, order.info['info'])
                for elemento in self.buy_records:
                    if elemento['atributo'] == order.info['info']:
                        self.buy_records.remove(elemento)
                self.sell_orders.append(order)  
                

    def stop(self):
        # Al final de la estrategia, imprime todas las órdenes
        print("Órdenes de Compra Completadas:")
        for order in self.buy_orders:
            print(order.data._name, order.executed.price)

        print("Órdenes de Venta Completadas:")
        for order in self.sell_orders:
            print(order.data._name, order.executed.price)
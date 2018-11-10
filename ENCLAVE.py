import socket
import json

from typing import Dict

listadionica = ["GS", "MS", "WFC", "VALBZ", "BOND", "VALE", "XLF"]

class Burza:
    def __init__ (self, test):

        if test:
            host_name = "test-exch-partitivnisumari"
            port = 25000
        else:
            host_name = "production"
            port = 25000

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host_name, port))
        self.stream = s.makefile('rw', 1)

        self.zapisi(("type": "hello", "team": 'PARTITIVNISUMARI'))
        assert self.citaj()['type'] == 'hello'
        self.order_id = 0

    def citaj(self, store_last=True):
        data = self.stream.readline()
        if(data == ""):
            return None
        else:
            data = json.loads(data)
            self.last_data = data
            !!!
        return data

    def zapisi(self, data):
        json.dump(data, self.stream)
        self.stream.write("\n")

    def kupi(self, buy_sell, symbol, price, size):
        trade = {'type': 'add', 'order_id': self.order_id,
                 'symbol': symbol, 'dir': buy_sell, 'price': price, 'size': size}
        self.order_id += 1

        if buy_sell == "SELL":
            self.zapisi(trade)
            !!!
        elif buy_sell == "BUY":
            self.zapisi(trade)
            !!!

def logger(dicc, ord):
    if ord['type'] == 'book':
        buy = ord['buy']
        sell = ord['sell']

        count_buy = 0
        value_buy = 0
        for p, n in buy:
            value_buy += p * n
            count_buy += n

        count_sell = 0
        value_sell = 0
        for p, n in sell:
            value_sell += p * n
            count_sell += n
        if count_buy != 0 and count_sell != 0:
            dicc[ord['symbol']].append((value_buy//count_buy, value_sell//count_sell))

def logN(burza, n):
    dicc = {}
    readed_results = []
    for i in range(n):
        readed_results.append(burza.citaj())
    for ord in readed_results:
        if ord['type'] == 'book':
            buy = ord['buy']
            sell = ord['sell']

            count_buy = 0
            value_buy = 0
            for p, n in buy:
                value_buy +=
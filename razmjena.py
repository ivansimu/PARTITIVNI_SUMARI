import socket
import json
import teste

from typing import Dict

tim = "PARTITIVNISUMARI"
listadionica = ["GS","MS", "WFC", "VALBZ","BOND","VALE","XLF"]

class Burza:
    def __init__(self, test):
        self.log = {} # symbol -> (prosjecna kupujuca cijena,prosjecna prodajna cijena)
        self.inv = {} # symbol -> broj dionica u invetoriju
        self.tradelog = {}
        for i in listadionica:
            self.log[i] = []
            self.tradelog[i] = []
            self.inv[i] = 0
        self.pendorders = {}
        if test:
            host_name = "test-exch-partitivnisumari"
            port = 25000
        else:
            host_name = "production"
            port = 25000

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host_name, port))
        self.stream = s.makefile('rw', 1)

        self.zapisi({"type": "hello", "team": tim})
        hello_exchange = self.citaj()
        assert hello_exchange['type'] == 'hello'

        self.order_id = 0


    def citaj(self, store_last=True):
        data = self.stream.readline()
        if(data == ""):
            return None
        else:
            data = json.loads(data)
            if store_last:
                self.last_data = data
                teste.logger(self.log,data)
                if data['type'] == 'fill':
                    if data['dir'] == 'BUY':
                        self.inv[data['symbol']] -= data['size']
                    else:
                        self.inv[data['symbol']] += data['size']
                elif data['type'] == 'trade':
                    self.tradelog[data['symbol']].append(data['price'])

            return data


    def zapisi(self, data):
        json.dump(data, self.stream)
        self.stream.write("\n")

    def kupi(self, buysell, symbol, price, size):
        trade = {'type': 'add', 'order_id': self.order_id, 'symbol': symbol,
                 'dir': buysell, 'price': price, 'size': size}
        self.order_id += 1
        #print(trade)
        if buysell == "SELL" and teste.shouldISell(self.inv,symbol):
            self.zapisi(trade)
            self.inv[symbol] -= size
        elif buysell == "BUY":
            self.zapisi(trade)
            self.inv[symbol] += size
        print(self.inv)


    def trade_batch(self, trades):
        # TODO provjeri konflikte
        for buysell, symbol, price, size in trades:
            if buysell and size != 0:
                self.zapisi(buysell, symbol, price, size)

    def pretvori(self, buysell, symbol, size):
        trade = {'type': 'convert', 'order_id': self.order_id,
                 'symbol': symbol, 'dir': buysell, 'size': size}
        self.order_id += 1
        print(trade)
        self.zapisi(trade)

import socket
import json

tim = "PARTITIVNISUMARI"

class Burza:
    def __init__(self, test):
        if test:
            host_name = "test-exch-partitivnisumari"
            port = 25001
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
            return data


    def zapisi(self, data):
        json.dump(data, self.stream)
        self.stream.write("\n")

    def kupi(self, buysell, symbol, price, size):
        trade = {'type': 'add', 'order_id': self.order_id, 'symbol': symbol,
                 'dir': buysell, 'price': price, 'size': size}
        self.order_id += 1
        print(trade)
        self.zapisi(trade)

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

import teste
from typing import Dict,List

listadionica = ["GS","MS", "WFC", "VALBZ","BOND","VALE","XLF"]

def run(burza):
    data = burza.last_data

    if data['type'] == 'book' and data['symbol'] == 'BOND':
        bidovi = data['buy']
        for price, size in bidovi:
            if price > 1000:
                burza.kupi('SELL', 'BOND', price, size)
        offeri = data['sell']
        for price, size in offeri:
            if price < 1000:
                burza.kupi('BUY', 'BOND', price, size)

def run2(burza):
    while True:
        burza.citaj()
        swicc(burza)

def run3(burza):
    # dffs = (symbol,int) -> int
    dffs = teste.alg(burza.log)
    data = burza.last_data
    sym = data['symbol']
    if data['type'] == 'book':
        if (sym,0) in dffs:
            bidovi = data['buy']
            for price, size in bidovi:
                if dffs[(sym,0)] > 0:
                    burza.kupi('SELL', sym, price, size)
            offeri = data['sell']
            for price, size in offeri:
                if dffs[(sym,1)] < 0:
                    burza.kupi('BUY', sym, price, size)

def swicc(burza):
    data = burza.last_data
    if data['type'] == 'book' and data['symbol'] == 'BOND':
        run2(burza)
    elif data['type'] == 'book' and data['symbol'] != 'BOND':
        skalpiranje(burza)


def skalpiranje(burza):

    narudzbe = []

    sizeVZ = 1
    sizeVE = 1

    stanje = {}

    while 'VALBZ' not in stanje and 'VALE' not in stanje:
        stanje = teste.logN(burza, 15)

    offerVZ = stanje['VALBZ'][3]
    bidVZ = stanje['VALBZ'][0]

    offerVE = stanje['VALE'][3]
    bidVE = stanje['VALE'][0]

    if offerVZ < bidVE - 10:
        burza.kupi('BUY', 'VALBZ', offerVZ, sizeVZ)
        burza.pretvori('BUY', 'VALE', sizeVZ)
        burza.kupi('SELL', 'VALE', bidVE, sizeVZ)


    if offerVE < bidVZ - 10:
        burza.kupi('BUY', 'VALE', offerVE, sizeVE)
        burza.pretvori('BUY', 'VALBZ', sizeVE)
        burza.kupi('SELL', 'VALBZ', bidVZ, sizeVE)

    return narudzbe

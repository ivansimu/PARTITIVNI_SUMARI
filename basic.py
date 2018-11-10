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
        run(burza)
    elif data['type'] == 'book' and data['symbol'] != 'BOND':
        skalpiranje(burza)
        skalpiranjeXLF(burza)


def skalpiranje(burza):

    narudzbe = []

    sizeVZ = 10
    sizeVE = 10

    stanje = {}

    while 'VALBZ' not in stanje or 'VALE' not in stanje:
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

def skalpiranjeXLF(burza):

    narudzbe = []

    sizeXLF = 20
    sizeBOND = 6
    sizeGS = 4
    sizeMS = 6
    sizeWFC = 4

    stanje = {}

    while ('XLF' not in stanje or 'BOND' not in stanje or 'GS' not in stanje or 'GS' not in stanje or
           'MS' not in stanje or 'WFC' not in stanje):
        stanje = teste.logN(burza, 15)

    offerXLF = stanje['XLF'][3]
    bidXLF = stanje['XLF'][0]

    offerBOND = stanje['BOND'][3]
    bidBOND = stanje['BOND'][0]

    offerGS = stanje['GS'][3]
    bidGS = stanje['GS'][0]

    offerMS = stanje['MS'][3]
    bidMS = stanje['MS'][0]

    offerWFC = stanje['WFC'][3]
    bidWFC = stanje['WFC'][0]

    if offerXLF < bidBOND + bidGS + bidMS + bidWFC - 100:
        burza.kupi('BUY', 'XLF', offerXLF, sizeXLF)
        burza.pretvori('SELL', 'XLF', sizeXLF)

        burza.kupi('SELL', 'BOND', bidBOND, sizeBOND)
        burza.kupi('SELL', 'GS', bidGS, sizeGS)
        burza.kupi('SELL', 'MS', bidMS, sizeMS)
        burza.kupi('SELL', 'WFC', bidWFC, sizeWFC)

    if offerBOND + offerGS + offerMS + offerWFC < bidXLF - 100:
        burza.kupi('BUY', 'BOND', offerBOND, sizeBOND)
        burza.kupi('BUY', 'GS', offerGS, sizeGS)
        burza.kupi('BUY', 'MS', offerMS, sizeMS)
        burza.kupi('BUY', 'WFC', offerWFC, sizeWFC)
        burza.pretvori('BUY', 'XLF', sizeXLF)

        burza.kupi('SELL', 'XLF', bidXLF, sizeXLF)

    return narudzbe

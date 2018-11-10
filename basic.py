import teste

def run(burza):

    narudzbe = []
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
    #print(narudzbe)
    return narudzbe

def run2(burza):
    while True:
        data = burza.citaj()
        run(burza)
        print(data)

def run3(burza):
    dffs = teste.alg(burza.log)
    data = burza.last_data
    sym = data['symbol']
    if data['type'] == 'book':
        if sym in dffs:
            bidovi = data['buy']
            for price, size in bidovi:
                if dffs[sym] < 0:
                    burza.kupi('SELL', sym, price, size)
            offeri = data['sell']
            for price, size in offeri:
                if dffs[sym] > 0:
                    burza.kupi('BUY', sym, price, size)

def swicc(burza):
    if data['type'] == 'book' and data['symbol'] == 'BOND':
        run2(burza)
    else if data['type'] == 'book' and data['symbol'] != 'GS' or 'MS' or 'WFC' or 'VALBZ':
        run3(burza)

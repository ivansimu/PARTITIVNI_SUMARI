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
        burza.citaj()
        swicc(burza)

def run3(burza):
    dffs = teste.alg(burza.log)
    data = burza.last_data
    sym = data['symbol']
    if data['type'] == 'book':
        if (sym,0) in dffs:
            bidovi = data['buy']
            for price, size in bidovi:
                if dffs[(sym,0)] < 0:
                    burza.kupi('SELL', sym, price, size)
            offeri = data['sell']
            for price, size in offeri:
                if dffs[(sym,1)] > 0:
                    burza.kupi('BUY', sym, price, size)

def swicc(burza):
    data = burza.last_data
    if data['type'] == 'book' and data['symbol'] == 'BOND':
        run2(burza)
    elif data['type'] == 'book': #and data['symbol'] == 'GS' or 'MS' or 'WFC' or 'VALBZ':
        run3(burza)

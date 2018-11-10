import teste

listadionica = ["GS","MS", "WFC", "VALBZ","BOND","VALE","XLF"]

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
        run(burza)

def run3(burza):
    dffs = teste.alg(burza.log,3)
    data = burza.last_data
    sym = data['symbol']
    if data['type'] == 'book':
        if (sym,0) in dffs:
            bidovi = data['buy']
            for price, size in bidovi:
                if dffs[(sym,0)] < 0 and teste.shouldISell(burza.inv, sym):
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
        return
        #run3(burza)


# def skalpiranje(burza):
#
                narudzbe = []

                data = burza.last_data
                if data['type'] == 'book' and data['symbol'] == 'VALBZ':
                    bidoviValbz = data['buy']
                    offeriValbz = data['sell']

                if data['type'] == 'book' and data['symbol'] == 'VALE':
                    bidoviVale = data['buy']
                    offeriVale = data['sell']
#
#     for bidVZ, sizeVZ in bidoviValbz:
#         for offerVE, sizeVE in offeriVale:
#             if offerVZ < bidVE - 10:
#                 burza.kupi('BUY', 'VALBZ', offerVZ, sizeVZ)
#                 burza.pretvori('BUY', 'VALE', sizeVZ)
#                 burza.kupi('SELL', 'VALE', bidVE, sizeVZ)
#
#     for bidVE, sizeVE in bidoviVale:
#         for offerVZ, sizeVZ in offeriValbz:
#             if offerVE < bidVZ - 10:
#                 burza.kupi('BUY', 'VALE', offerVE, sizeVE)
#                 burza.pretvori('BUY', 'VALBZ', sizeVE)
#                 burza.kupi('SELL', 'VALBZ', bidVZ, sizeVE)
#
#     return narudzbe

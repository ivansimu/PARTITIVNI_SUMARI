def run(burza):

    narudzbe = []
    data = burza.last_data

    if data['type'] == 'book' and data['symbol'] == 'BOND':
        bidovi = data['buy']
        for price, size in bidovi:
            if price > 1000:
                narudzbe.append(('SELL', 'BOND', price, size))
        offeri = data['sell']
        for price, size in offeri:
            if price < 1000:
                narudzbe.append(('BUY', 'BOND', price, size))
    print(narudzbe)
    map(lambda z,x,c,v: burza.kupi(z,x,c,v),narudzbe)
    return narudzbe

def run2(burza):
    while True:
        data = burza.citaj()
        run(burza)
        print(data)

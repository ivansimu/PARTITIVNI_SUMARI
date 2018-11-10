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

    return narudzbe

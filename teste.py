def logger(d,ord):
    if ord['type'] == 'book':
        # print(ord)
        # print(d)
        # print(ord['symbol'])
        # print(d[ord['symbol']])
        buy = ord['buy']
        sell = ord['sell']

        tb = 0
        cb = 0
        for p,n in buy:
            cb += p * n
            tb += n

        ts,cs = 0,0
        for p,n in sell:
            cs += p * n
            ts += n
        if tb != 0 and ts != 0:
            d[ord['symbol']].append((cb//tb,cs//ts)) # cb//tb - prosjecna cijena kupnje, cs//ts - prosjecna cijena prodaje

def logN(burza,n):
    d = {}
    ords = []
    for i in range(n):
        ords.append(burza.citaj())
    for ord in ords:
        if ord['type'] == 'book':
            buy = ord['buy']
            sell = ord['sell']
            print(buy)
            tb = 0
            cb = 0
            for p,n in buy:
                cb += p * n
                tb += n

            ts,cs = 0,0
            for p,n in sell:
                cs += p * n
                ts += n

            if tb != 0 and ts != 0:
                d[ord['symbol']] = (max(map(lambda x: x[0],buy)),min(map(lambda x: x[0],buy)),
                                    max(map(lambda x: x[0],sell)),min(map(lambda x: x[0],sell)),cb//tb,cs//ts) # cb//tb - prosjecna cijena kupnje, cs//ts - prosjecna cijena prodaje
    return d


listadionica = ["GS","MS", "WFC", "VALBZ","BOND","VALE","XLF"]

def alg(d,mx=11):
    res = {}
    diffs = []
    #print(d)
    for sym in listadionica:
        prices = d[sym]
        j: int
        for j in [0,1]:
            prices = list(reversed(prices[len(prices)- mx * (mx + 1) // 2:])) #uzmi zadnjih mx *(mx-1) i okreni listu
            n = 1
            i = 0
            while i + n < len(prices) and n <= mx:
                diffs.append(prices[i+n][j] - prices[i][j])
                i += n
                n += 1
            if len(diffs) > 0:
                res[(sym,j)] = sum(diffs)//len(diffs)
            diffs.clear()
    return res

# def shouldIBuy(inv, symbol):
#     if symbol in ['GS', 'MS', 'WFC', 'XLF'] and inv[symbol] >= 0 and inv[symbol] <= 100:
#         return True
#     elif symbol in ['VALBZ', 'VALE'] and inv[symbol] >= 0 and inv[symbol] <= 10:
#         return True
#     elif symbol == 'BOND':
#         return True
#     else:
#         return False

def shouldISell(inv, symbol):
    if symbol in ['GS', 'MS', 'WFC', 'XLF', 'VALBZ', 'VALE'] and inv[symbol] >= 0:
        return True
    else:
        return False

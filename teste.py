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
        d[ord['symbol']].append((cb//tb,cs//ts))

def alg(d,mx=11):
    res = {}
    diffs = []
    for sym,prices in d:
        j: int
        for j in [0,1]:
            prices = list(reversed(prices))
            n = 1
            i = 0
            while i + n < len(prices) and n <= mx:
                diffs.append((prices[i+n][j] - prices[i][j])//2)
                i += n
                n += 1
            res[(sym,j)] = sum(diffs)//len(diffs)
            diffs.clear()
    return res

def shouldIBuy(inv, symbol):
    if symbol in ['GS', 'MS', 'WFC', 'XLF'] and inv[symbol] >= 0 and inv[symbol] <= 100:
        return True
    elif symbol in ['VALBZ', 'VALE'] and inv[symbol] >= 0 and inv[symbol] <= 10:
        return True
    elif symbol == 'BOND':
        return True
    else:
        return False

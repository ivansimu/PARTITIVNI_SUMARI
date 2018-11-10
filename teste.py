def logger(d,ord):
    if ord['type'] == 'book':
        print(ord)
        print(d)
        print(ord['symbol'])
        print(d[ord['symbol']])
        d[ord['symbol']].append(ord['price'])

def alg(d,mx=11):
    res = {}
    diffs = []
    for sym,prices in d:
        prices = reversed(prices)
        n = 1
        i = 0
        while i + n < len(prices) and n <= mx:
            diffs.append((prices[i+n] - prices[i])//2)
            i += n
            n += 1
        res[sym] = sum(diffs)//len(diffs)
        diffs.clear()
    return res
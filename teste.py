def logger(d,ord):
    print(d,ord)
    if ord['type'] == 'book':
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
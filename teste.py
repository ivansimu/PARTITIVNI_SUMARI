def logger(d,ord):
    d[ord['symbol']].extend(ord['price'])

def alg(d):
    res = []
    diffs = []
    for sym,prices in d:
        prices = reversed(prices)
        n = 1
        i = 0
        while i + n < len(prices):
            diffs.append((prices[i+n] - prices[i])//2)
            i += n
            n += 1
        res.append((sym,sum(diffs)//len(diffs)))
        diffs.clear()
    return res
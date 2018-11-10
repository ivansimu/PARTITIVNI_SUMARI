def logger(d,ord):
    d[ord['symbol']].extend(ord['price'])

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
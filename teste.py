def logger(d,ord):
    d[ord['symbol']].extend(ord['price'])

def alg(d):
    diffs = []
    for sym,prices in d:
        for p in prices:
            if p

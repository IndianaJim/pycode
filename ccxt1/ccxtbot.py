import ccxt

def style(s, style):
    return style + s + '\033[0m'


def green(s):
    return style(s, '\033[92m')


def blue(s):
    return style(s, '\033[94m')


def yellow(s):
    return style(s, '\033[93m')


def red(s):
    return style(s, '\033[91m')


def pink(s):
    return style(s, '\033[95m')


def bold(s):
    return style(s, '\033[1m')


def underline(s):
    return style(s, '\033[4m')


def dump(*args):
    print('\n')
    print(' '.join([str(arg) for arg in args]))

exchanges = ccxt.exchanges

#for exchange in exchanges:
   # print(exchange)

exchange = ccxt.coinbasepro()

symbol = 'BTC/USD'
ticker = exchange.fetch_ticker(symbol.upper())
print(ticker)
dump(
    green(exchange.id),
    yellow(symbol),
    'ticker',
    ticker['datetime'],
    'high: ' + str(ticker['high']),
    'low: ' + str(ticker['low']),
    'bid: ' + str(ticker['bid']),
    'ask: ' + str(ticker['ask']),
    'volume: ' + str(ticker['quoteVolume']))



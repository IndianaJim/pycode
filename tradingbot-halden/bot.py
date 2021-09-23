import krakenex
import json
import time
import datetime
import calendar

def get_crypto_data(pair, since):
    return api.query_public('OHLC', data = {'pair': pair, 'since': since})['result'][pair]

def get_balance():
    return api.query_private('Balance') #remove if no balance yet...  ['result']

def analyze(pair,since):
    data = get_crypto_data(pair[0]+pair[1],since)
    lowest = 0
    highest = 0
    for prices in data:
        balance = get_fake_balance()
        last_trade = get_last_trade(pair[0]+pair[1])
        last_trade_price = float(last_trade['price'])
        open_ = float(prices[1])
        high_ = float(prices[2])
        low_ = float(prices[3])
        close_ = float(prices[4])

        did_sell = False

        try:
            balance[pair[0]]
            # if i own any of the pair currency, then check for sell
            selling_point_win = last_trade_price * 1.005
            selling_point_loss = last_trade_price * 0.995
            #selling ata win
            if open_ >= selling_point_win or close_ >= selling_point_win:
                #sell at a profit
                did_sell = True
                fake_sell(pair[0]+pair[1], close_, last_trade)
            elif open_ <= selling_point_loss or close_ <= selling_point_loss:
                #sell at aloss
                did_sell = True
                fake_sell(pair[0]+pair[1], close_, last_trade)

            #logic for if we should buy
            if not did_sell and float(balance['USD.HOLD']) > 0:
                if low_ < lowest or lowest == 0:
                    lowest = low_
                if high_ > highest:
                    highest = high_

            price_to_buy = 1.0005

            if highest/lowest >= price_to_buy and low_ <= lowest:
                available_money = balance['USD.HOLD']
                # buy method
                fake_buy(pair[0]+pair[1], available_money, close_, last_trade)

def fake_buy(pair, dollar_amount, close_, last_trade):
    trades_history = get_fake_trades_history()
    last_trade['price'] = str(close_)
    last_trade['type'] = 'buy'
    last_trade['cost'] = dollar_amount
    last_trade['time'] = datetime.datetime.now().timestamp()
    last_trade['vol'] = str(float(dollar_amount)/close_)
    
def fake_sell(pair, close_, last_trade):
    trades_history = {}



def get_fake_balance():
    with open('balance.json','r') as f:
        return json.load(f)

def get_fake_trades_history():
    with open('tradeshistory.json', 'r') as f:
        return json.load(f)

def get_trades_history():
    start_date = datetime.datetime(2021,7,4)
    end_date = datetime.datetime.today()
    return api.query_private('TradesHistory',req(start_date,end_date,1))['result']['trades']

def get_last_trade(pair):
    trades_history = get_fake_trades_history()
    last_trade = {}
    for trade in trades_history:
        trade = trades_history[trade]
        if trade['pair'] == pair and trade['type'] == 'buy':
            last_trade = trade
    return last_trade

def date_nix(str_date):
    return calendar.timegm(str_date.timetuple())

def req(start, end, ofs):
    req_data = {
        'type':'all',
        'trades':'true',
        'start':str(date_nix(start)),
        'end':str(date_nix(end)),
        'ofs':str(ofs) 
    }
    return req_data

if __name__ == '__main__':
    api = krakenex.API()
    api.load_key('d:\\py\\apikeys\\kraken.key')
    pair=('XETH','ZUSD')
    since=str(int(time.time() - 3600))
    #print(json.dumps(get_crypto_data(pair, since), indent=4))
    print(json.dumps(get_fake_trades_history(), indent=4))



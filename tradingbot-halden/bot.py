import krakenex
import json
import time
import datetime
import calendar

def get_crypto_data(pair, since):
    return api.query_public('OHLC', data = {'pair': pair, 'since': since})['result'][pair]

def get_balance():
    return api.query_private('Balance') #remove if no balance yet...  ['result']

def get_traddes_history():
    return 0

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
    pair='XETHZUSD'
    since=str(int(time.time() - 3600))
    #print(json.dumps(get_crypto_data(pair, since), indent=4))
    print(json.dumps(get_balance(), indent=4))




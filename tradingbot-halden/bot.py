import krakenex
import json
import time
import datetime
import calendar

api = krakenex.API()
api.load_key('d:\\py\\apikeys\\kraken.key')
pair='XETHZUSD'
since=str(int(time.time() - 3600))

print(json.dumps(api.query_public('OHLC', data = {'pair': pair, 'since': since}), indent=4))



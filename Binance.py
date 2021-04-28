from binance.client import Client 
from binance.websockets import BinanceSocketManager
import pandas as pd
import time
import json

api_key = "uBqSAbUQZaY7fyfWuktpGMlis8GsIP5LGkM2SHnJpIg70g7dAwatOC1fkbeQ826o"
api_secret = "sxp8145OlFKLVlwcNbhfnkJhzCDSL4Ma0y4zUVivNVrN9uS8gsBOViioeAzqBsiG"

client = Client(api_key,api_secret)
contador = 0

#data = []

def process_message(msg):
    global contador
    if contador == 1:
     #   data.append(
      #      {
       #         'symbol' : msg['s'],
        #        'bid' : msg['b'],
         #       'ask' : msg['a'],
          #      'percent' : msg['P'],
           #     'diff' : msg['p']
            #}
        #)
        
        with open('./logstash/logs/data.text', 'a') as outfile:
            #json.dump(data, outfile)
            outfile.write("Bid - Ask ADAEUR price: {} - {} - {} - {}\n".format(msg['b'], msg['a'], msg['p'], msg['P']))

        print("Bid - Ask ADAEUR price: {} - {} - {} - {}\n".format(msg['b'], msg['a'], msg['p'], msg['P']))
        
        contador = 0
    else:
        contador+=1

bm = BinanceSocketManager(client)
bm.start_symbol_ticker_socket('ADAEUR', process_message)
bm.start()

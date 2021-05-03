from binance.client import Client 
from binance.websockets import BinanceSocketManager
import time
import json
import datetime


api_key = "uBqSAbUQZaY7fyfWuktpGMlis8GsIP5LGkM2SHnJpIg70g7dAwatOC1fkbeQ826o"
api_secret = "sxp8145OlFKLVlwcNbhfnkJhzCDSL4Ma0y4zUVivNVrN9uS8gsBOViioeAzqBsiG"

client = Client(api_key,api_secret)
contador = 0

def process_message(msg):
    global contador
    if contador == 3:
        with open('data.txt', 'a') as outfile:
            fecha = datetime.datetime.fromtimestamp(msg['E']/1000.0)

            outfile.write("{} Bid - Ask ADAEUR price: {} - {} - {} - {}\n".format(fecha, msg['b'], msg['a'], msg['p'], msg['P']))
            
            print("{} Bid - Ask ADAEUR price: {} - {} - {} - {}\n".format(fecha, msg['b'], msg['a'], msg['p'], msg['P']))

            contador = 0
    else:
        contador+=1

bm = BinanceSocketManager(client)
bm.start_symbol_ticker_socket('ADAEUR', process_message)
bm.start()

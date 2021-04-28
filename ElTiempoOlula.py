#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

def get_time(url="https://api.tutiempo.net/json/?lan=es&apid=4xYXzXzX4a4falf&lid=7698"):
    
    response = requests.get(url)
    
    if response.status_code == 200:
        payload = response.json()
        print(payload.get("copyright"))
        results = payload.get('results',[])
        
        if results:
            for datos in results:
              #  name = datos['name']
                print(datos)
                            
if __name__ == '__main__':
    url = "https://api.tutiempo.net/json/?lan=es&apid=4xYXzXzX4a4falf&lid=7698"
    get_time(url)
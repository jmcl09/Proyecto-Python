<center><h1>Tracking Binance API con Python</h1></center>

<h1>1. Requisitos</h1>

Necesitaremos:

- Python instalado
- Binance Library
- Api key / Api secret procedente de Binance

<h2>1.1 Instalación</h2>

<h4>Unix</h4>

Instalamos python3:

```bash
yum install -y python3
```

Instalamos pip (nos permitirá instalar las librerías necesarias):

```bash
python3 -m pip install -U pip
```

Instalaremos setuptools, necesario para varias librerías:

```bash
python3 -m pip install -U setuptools
```

Instalaremos la librería de binance:

```bash
pip install python-binance
```

<h4>Windows</h4>

Instalamos python:

```
https://www.python.org/ftp/python/3.9.4/python-3.9.4-amd64.exe
```

Instalamos las librerías necesarias:

```bash
pip install python-binance
```

<h1>2. Código</h1>

Necesitaremos importar las librerías que usaremos, entre ellas usaremos **binance.client** que nos permitirá conectarnos como clientes a Binance:

```python
from binance.client import Client 
from binance.websockets import BinanceSocketManager
import time
import json
```

Definiremos dos variables globales las cuales serán nuestra clave de Api pública y privada (cada uno tiene su propia clave):

```python
api_key ="uBqSAbUQZaY7fyfWuktpGMlis8GsIP5LGkM2SHnJpIg70g7dAwatOC1fkbeQ826o"
api_secret ="sxp8145OlFKLVlwcNbhfnkJhzCDSL4Ma0y4zUVivNVrN9uS8gsBOViioeAzqBsiG"
```

Hacemos la conexión a la Api creando con ella una variable que nos permitirá interactuar con la conexión y una variable contador que nos permitirá escribir logs cada x tiempo:

```python
client = Client(api_key,api_secret)
contador = 0
```

Definiremos la función **process_message** que nos mostrará el mensaje obtenido de la api, además de escribir ese mensaje cada x tiempo y obtener los valores que nosotros queramos:

```python
def process_message(msg):
    global contador
    if contador == 60:
        with open('data.txt', 'a') as outfile:
            outfile.write("Bid - Ask ADAEUR price: {} - {} - {} - {}\n".format(msg['b'], msg['a'], msg['p'], msg['P']))

        print("Bid - Ask ADAEUR price: {} - {} - {} - {}\n".format(msg['b'], msg['a'], msg['p'], msg['P']))
        
        contador = 0
    else:
        contador+=1
```

Como podemos observar la función hace referencia a la variable contador que tenemos declarada fuera, y comprueba que la variable sea igual a 60, en caso afirmativo entrará y escribirá en el fichero data.txt la siguiente línea:

```python
"Bid - Ask ADAEUR price: {} - {} - {} - {}\n".format(msg['b'], msg['a'], msg['p'], msg['P'])
```

Esto nos escribirá algo así:

```
Bid - Ask ADAEUR price: 1.10580000 - 1.10620000 - 0.05610000 - 5.343
```

Siendo:

- **msg['b']:** Bid, el mejor precio de compra de la criptomoneda.
- **msg['a']:** Ask, el mejor precio de venta de la criptomoneda.
- **msg['p']:** La diferencia de precio respecto al valor anterior de la moneda (el cambio).
- **msg['P']:** Percent, el porcentaje de cambio del valor de la moneda.

En caso negativo, incrementaría el valor de contador 1 más. Esto realmente lo que hace es contar cuantas veces está trayendo la información de la API, por defecto actualiza la información una vez por segundo, con esto estamos escribiendo el cambio una vez cada 60 eventos, o cada 60 segundos.. 

Y por último y no menos importante, el núcleo de nuestra app:

```python
bm = BinanceSocketManager(client)
bm.start_symbol_ticker_socket('ADAEUR', process_message)
bm.start()
```

Declaramos un objeto de tipo BinanceSocketManager con la conexión cliente, y empezamos la lectura de API por tick (segundo) indicándole la moneda que queremos trackear, en este caso **ADAEUR** siendo la moneda ADA y mostrándola en EURos (€), y a continuación hacemos la llamada al método.

<h1>3. Funcionamiento</h1>

Para poder hacer funcionar este script, deberemos ejecutar el siguiente comando:

<h4>Windows
</h4>

```bash
py Binance.py
```

<h4>Unix</h4>

```bash
python3 Binance.py
```

Y empezará a escribir la información en nuestro txt.

<h1>
    4. Autor
</h1>

<h4>José Manuel Cruzado Lorente.</h4>

<h4>29/04/2021</h4>


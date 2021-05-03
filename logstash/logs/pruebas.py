import json
import requests
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient

# Conexión a Elasticsearch
conexion = Elasticsearch(["elasticsearch:9200"])

# Establecer conexión con los Indices
ci = IndicesClient(conexion)

# Borrar índice
#print(es.indices.delete(index="adaeu*"))

# Obtener información del indice
#print(ci.get("adaeu-2021.04.29"))

# Poner Alias
#print(ci.put_alias("adaeu-2021.04.29","cardano"))

# Obtener iformación desde el alias
#print(ci.get("cardano"))

# Insertar datos
with open("datos.json", "r") as f:  
    contenido = f.read()
    data = contenido.replace('[',' ')
    data = data.replace(']',' ')
    data = data.split('}')

    
    data[0]+=('}')
    
    #final = json.loads(data)
    
print(data[1])




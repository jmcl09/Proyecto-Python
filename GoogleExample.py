import requests

if __name__ == "__main__":
    url = "https://www.google.com/"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(response.content) #Muestra el HTML de la página
        
        #file = open('google.html', 'wb') #Crea un archivo de escritura binaria llamado google.html
        #file.write(content) #Escribe el HTML obtenido de la respuesta
        #file.close() #Cerramos el flujo
    
        #print(response) #Imprime el código de respuesta
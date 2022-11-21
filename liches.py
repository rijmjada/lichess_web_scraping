# Instalar librerias: Pandas, Request, BS4, Lxml

# Importar las librerias instaladas

import pandas as pd
import requests
from bs4 import BeautifulSoup


# Guardo en una variable llamada 'web', la pagina web de donde voy a extraer la información
web = 'https://lichess.org/player'


# Hago una petición a dicha pagina con el metodo requests.get() y lo guardo en la variable 'response'
response = requests.get(web)


# En la variable content guardo el texto que tiene ese response
content = response.text


# Genero una instancia de BS4 - Recibe como parametros el content y el parser (en este caso lxml)
soup = BeautifulSoup(content, 'lxml')


# Metodo 'find_all()' recibe como parametro la etiqueta html y clase a la que pertenece dicha etiqueta
# Declaro la variable 'lista_secciones' que guardara la respuesta del metodo 'find_all()'
lista_secciones = soup.find_all('section', class_='user-top')


# Declaro una variable 'list_players' que contendra el listado de jugadores.
list_players = []


# Recorro la lista de secciones y extraigo los datos para appendearlos a la lista de jugadores
for i in lista_secciones:
    list_players.append('\n')
    for j in i:
        for k in j:
            list_players.append(k.get_text(strip=True, separator=' '))


# Por ultimo genero un DataFrame para poder exportar esta lista a un archivo .csv
datos = pd.DataFrame(list_players)
datos.to_csv('Clasificaciones.csv', index=False, header=False, quotechar=' ')

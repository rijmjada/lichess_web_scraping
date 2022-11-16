import json
import pandas as pd
import requests
from bs4 import BeautifulSoup

web = 'https://lichess.org/player'
response = requests.get(web)
content = response.text

soup = BeautifulSoup(content, 'lxml')

lista_secciones = soup.find_all('section', class_='user-top')

list_players = []

for i in lista_secciones:
    list_players.append('\n')
    for j in i:
        for k in j:
            list_players.append(k.get_text(strip=True, separator=' '))
            

datos = pd.DataFrame(list_players)
datos.to_csv('Clasificaciones.csv', index=False, header=False, quotechar=' ')

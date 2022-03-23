import requests
from bs4 import BeautifulSoup
from datetime import *
from os import path, mkdir, makedirs
import logging

dic_csv = {'museos':
           'https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_4207def0-2ff7-41d5-9095-d42ae8207a5d',
           'cines':
           'https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_392ce1a8-ef11-4776-b280-6f1c7fae16ae' ,
           'bibliotecas': 
           'https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_01c6c048-dbeb-44e0-8efa-6944f73715d7'}

list_save=[]

for k, v in dic_csv.items():
    r = requests.get(v)
    r.encoding = 'utf-8'
    parse = BeautifulSoup(r.text, 'html.parser')
    links = parse.find_all('div', {'class':'col-md-2 col-xs-12 resource-actions'})
    fecha = datetime.today().strftime('%d-%m-%Y')
    
    for link in links:
        data = link.find('a').attrs['href']
        r = requests.get(data, allow_redirects=True)
        file_path= path.join(k, datetime.today().strftime('%Y-%B'))
        file = k + "-" + fecha + ".csv"
        
        if not path.isdir(file_path):
                makedirs(file_path)
                logging.info('Create directory')
                
        print(file_path)
        save = path.join(file_path, file)
        list_save.append(save)
        print(list_save)
        open(save, 'wb').write(r.content)
        logging.info('File Downloaded')
            
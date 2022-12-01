import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

NUMBER_PAGES = 9
IPHONE = '11'
GB = '64'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/107.0.0.0 Safari/537.36'}

dic_produtos = {'marca': [], 'preco': []}


for i in range(NUMBER_PAGES):
    url_page = f'https://pb.olx.com.br/celulares/iphone?o={i+1}&elbh=1&elcd=1'
    site = requests.get(url_page, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    Itens = soup.find_all('li', class_=re.compile('dvcyfD'))

    for item in Itens:
        try:
            title = item.find('h2', class_=re.compile('iUMNkO')).get_text().strip()
            price = item.find('span', class_=re.compile('jViSDP')).get_text().strip()

            if IPHONE in title and GB in title:
                dic_produtos['marca'].append(title)
                dic_produtos['preco'].append(price[3:])
        except Exception as e:
            print(e)

print(dic_produtos)
df = pd.DataFrame(dic_produtos)
df.to_excel('C:\\Users\\artur\\Downloads\\iphone.xlsx', index=False)

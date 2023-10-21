import requests
from bs4 import BeautifulSoup
import math
import re

url = "https://www.vivareal.com.br/venda/paraiba/joao-pessoa/bairros/bessa/apartamento_residencial/?pagina=2"

headers = {"User-Agente": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

qtd_itens = soup.find('strong', class_='results-summary__count js-total-records').get_text().strip()

index = math.ceil(int(qtd_itens.replace('.', ''))/36)

dic_imoveis = {'endereço': [], 'm2': [], 'qtd_quartos': [], 'qtd_banheiros': [], 'qtd_vagas': [], 'valor': [], 'condominio': []}


for i in range(1, index+1)[:2]:
    print(i)
    url_page = f"https://www.vivareal.com.br/venda/paraiba/joao-pessoa/bairros/bessa/apartamento_residencial?pagina={i}" 
    site = requests.get(url_page, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    imoveis = soup.find_all('article', class_='js-property-card')

    for imovel in imoveis[:2]:
        rua = imovel.find('span', class_='property-card__address').get_text().strip()
        print(rua)
import requests
from bs4 import BeautifulSoup

url = 'https://www.placardefutebol.com.br/jogos-em-andamento'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

for jogo in soup.find_all('div',class_='row align-items-center content'):
    # resultados_fora = soup.find_all('div', class_="w-25 p-1 match-score d-flex justify-content-start")
    # for i in resultados_fora:
    #     print(i.get_text().strip())
    print(jogo.get_text().strip())
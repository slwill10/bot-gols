import requests
from bs4 import BeautifulSoup

url = 'https://www.placardefutebol.com.br/jogos-em-andamento'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

for jogo in soup.find_all('div',class_='row row-fix'):
    print(jogo.get_text().strip())
import time
import requests
from bs4 import BeautifulSoup

# URL do site de jogos ao vivo
url = 'https://www.placardefutebol.com.br/jogos-em-andamento'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
# }
# print(soup.find_all('h5', class_="text-right team_link")) 
# title = soup.find_all('h3', class_="match-list_league-name")
# time_casa = soup.find_all('h5', class_="text-right team_link")
# jogos = soup.find_all('div', id='livescore')
# for tag in jogos:
#     time_casa = soup.find_all('h5', class_="text-right team_link")
    # time_visitante = soup.find_all('h5', class_="text-left team_link")     
    # result_casa = soup.find_all('div', class_='w-25 p-1 match-score d-flex justify-content-start')
    # result_visitante = soup.find_all('div', class_='w-25 p-1 match-score d-flex justify-content-end')
    
# return [tag[time_casa]]


# title = soup.find('div', class_="row linhaPartida")

# tempo= []
# time_casa = []
# time_fora = []
# result_casa = []
# result_fora = []

# for x in soup.find_all('div', id="livescore"):
#     tempo = soup.find_all('span', class_='badge badge-success status-name blink')
#     for t in tempo:
#         tempo.append(t)
#         print(t.get_text())
#     time_casa = soup.find_all('h5', class_="text-right team_link")
#     for time in time_casa:
#         print(time.get_text())
#     time_fora = soup.find_all('h5', class_='text-left team_link')
#     for fora in time_fora:
#         print(fora.get_text())
#     result_casa = soup.find_all('span', class_="badge badge-default")
#     for result_c in result_casa:
#         print(result_c.get_text())
#     result_fora = soup.find_all('span', class_='badge badge-default')
#     for result_f in result_fora:
#         print(result_f.get_text())
    
#     mensagem_final += f"{tempo.get_text()} {result_c.get_text()} x {result_f.get_text()} {fora.get_text()} \n"

# print(mensagem_final)

mensagem_final = ""

# Faz a pesquisa uma vez e usa as variáveis para armazenar as listas corretas
tempos = soup.find_all('span', class_='badge badge-success status-name blink')
times_casa = soup.find_all('h5', class_="text-right team_link")
times_fora = soup.find_all('h5', class_='text-left team_link')
resultados_casa = soup.find_all('div', class_="w-25 p-1 match-score d-flex justify-content-end")
resultados_fora = soup.find_all('div', class_="w-25 p-1 match-score d-flex justify-content-start")

# Itera sobre as partidas encontradas
for i in range(len(tempos)):
            tempo = tempos[i].get_text().strip()
            time_casa = times_casa[i].get_text()  # Pega o nome do time da casa
            time_fora = times_fora[i].get_text()  # Pega o nome do time de fora
            resultado_casa = resultados_casa[i].get_text().strip()  # Pega o placar da casa
            resultado_fora = resultados_fora[i].get_text().strip() # Pega o placar do visitante

            penaltis_casa = resultados_casa[i].find('span', class_='badge badge-penalties')
            penaltis_fora = resultados_fora[i].find('span', class_='badge badge-penalties')

            if penaltis_casa and penaltis_fora:
                    resultado_casa = penaltis_casa.get_text().strip()
                    resultado_fora = penaltis_fora.get_text().strip()


            # Concatena as informações na mensagem final
            mensagem_final += f"{tempo} {time_casa} {resultado_casa} x {resultado_fora} {time_fora}\n"

# Exibe a mensagem final
print(mensagem_final)

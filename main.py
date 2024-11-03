import time
import requests
from bs4 import BeautifulSoup
from envio_telegram import *


# Função para buscar os dados dos jogos
def buscar_dados_jogos():
    url = 'https://www.placardefutebol.com.br/jogos-em-andamento'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    jogos = []

    # Faz a pesquisa uma vez e usa as variáveis para armazenar as listas corretas
    tempos = soup.find_all('span', class_='badge badge-success status-name blink')
    times_casa = soup.find_all('h5', class_="text-right team_link")
    times_fora = soup.find_all('h5', class_='text-left team_link')
    resultados_casa = soup.find_all('div', class_="w-25 p-1 match-score d-flex justify-content-end")
    resultados_fora = soup.find_all('div', class_="w-25 p-1 match-score d-flex justify-content-start")

    for i in range(len(tempos)):
        tempo = tempos[i].get_text().strip()
        time_casa = times_casa[i].get_text().strip()
        time_fora = times_fora[i].get_text().strip()
        resultado_casa = resultados_casa[i].get_text().strip()
        resultado_fora = resultados_fora[i].get_text().strip()

        jogos.append({
            'tempo': tempo,
            'time_casa': time_casa,
            'time_fora': time_fora,
            'resultado_casa': resultado_casa,
            'resultado_fora': resultado_fora
        })
    
    return jogos

# Função para comparar os jogos e verificar se houve gol
def verificar_mudanca(jogos_anteriores, jogos_atualizados):
    mudancas = []
    
    for i in range(len(jogos_atualizados)):
        jogo_anterior = jogos_anteriores[i]
        jogo_atual = jogos_atualizados[i]
        
        if jogo_anterior['resultado_casa'] != jogo_atual['resultado_casa'] or jogo_anterior['resultado_fora'] != jogo_atual['resultado_fora']:
            mudancas.append(jogo_atual)
    
    return mudancas

# Loop principal
jogos_anteriores = buscar_dados_jogos()

while True:
    time.sleep(20)  # Aguardar 20 segundos antes de verificar novamente
    jogos_atualizados = buscar_dados_jogos()
    
    mudancas = verificar_mudanca(jogos_anteriores, jogos_atualizados)
    
    if mudancas:
        mensagem_final = ""
        for jogo in mudancas:
            mensagem_final += f"⚽ {jogo['tempo']} {jogo['time_casa']} {jogo['resultado_casa']} x {jogo['resultado_fora']} {jogo['time_fora']}\n"
        
        print(mensagem_final)  # Aqui você poderia enviar a mensagem via Telegram ou outro canal de notificação
        response = send_message(token, chat_id, mensagem_final)
        print(response)
    # Atualizar o estado anterior dos jogos
    jogos_anteriores = jogos_atualizados

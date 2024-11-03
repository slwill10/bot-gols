import telegram
import requests

# Substitua pelo seu token e chat_id do Telegram
token = '7587016499:AAEz_rv4KTpUyEnLZFsKUnhNAKKxospuB9o'
chat_id = '6266814093'
bot = telegram.Bot(token=token)

def send_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=payload)
    return response.json()
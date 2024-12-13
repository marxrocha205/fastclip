import requests

def send_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print("Mensagem enviada com sucesso!")
        
    else:
        print(f"Falha ao enviar a mensagem: {response.status_code}, {response.text}")

# Seu token de API fornecido pelo BotFather
TOKEN = '7005335494:AAHexvYW5zK0joKKd5IWWLjICm0HhWnjkgc'
# O ID do chat que você acabou de obter
CHAT_ID = '-4558544984'


# Envia a mensaVIVA
def chamar (MESSAGE) :
    send_message(TOKEN, CHAT_ID, MESSAGE)


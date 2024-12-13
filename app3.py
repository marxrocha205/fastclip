import cv2
import pytesseract
import numpy as np
import time
from telegram import chamar
from connect import * 
from teste import * 

# Lista de URLs dos vídeos
video_urls = {
    "PE1VIVA": "https://s3.us-east-1.wasabisys.com/mediapro-dev/PE1VIVA.mp4"
}

# Lista de frases-alvo
target_phrases = ["Sinal não encontrado", "no signal", "Confira a Oferta!"]

def log_message(message):
    chamar(message)

def check_video_for_phrase_and_consistency(video_key, video_url, target_phrases):
    print(f"Analisando vídeo: {video_url}")
    cap = cv2.VideoCapture(video_url)
    frame_count = 0
    errorVid = False
    
    video = video_key[:2]
    channel = video_key[2:].lower()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        # Converter frame para escala de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Aplicar OCR no frame
        text = pytesseract.image_to_string(gray, lang='por+eng')
        # Verificar se alguma frase está no texto reconhecido
        if any(phrase in text for phrase in target_phrases):
            error_vids('Problema detectado', video, video_url, channel, video_key)
            cap.release()
            return True  # Retornar para garantir que o loop principal continue

    cap.release()
    return False  # Se não encontrou problemas, retornar False
    
def error_vids(error, key, video, channel, video_key): 
    if video_key[:3] in ['CUR', 'CAM']:
        log_message(f'{error} {video}')
        obter(video_key[:3], video_key[3:].lower())
    else:
        log_message(f'{error} {video}')
        obter(key, channel)

def main():
    while True:  # Loop infinito para rodar indefinidamente
        for video_key, video_url in video_urls.items():
            # Verificar o vídeo diretamente da URL
            found = check_video_for_phrase_and_consistency(video_key, video_url, target_phrases)
            if not found:
                print(f"Frase não encontrada no vídeo {video_key}")
        # Pausar por 30 minutos (1800 segundos) antes de analisar novamente
        print("Aguardando 30 minutos antes da próxima análise...")
        time.sleep(3600)

if __name__ == "__main__":
    main()

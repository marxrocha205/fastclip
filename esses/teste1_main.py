import cv2
import pytesseract
import numpy as np
import time
from telegram import chamar
from testeconnect import * 
from testeffmpeg import * 
from testeblue import *
# Lista de URLs dos vídeos
video_urls = {

   "BHGNT": "https://s3.us-east-1.wasabisys.com/mediapro-dev/BHGNT.mp4",
   "BHGNW": "https://s3.us-east-1.wasabisys.com/mediapro-dev/BHGNW.mp4",
   "BHSPO": "https://s3.us-east-1.wasabisys.com/mediapro-dev/BHSPO.mp4",
   "BHMSW": "https://s3.us-east-1.wasabisys.com/mediapro-dev/BHMSW.mp4",
   "BHVIVA": "https://s3.us-east-1.wasabisys.com/mediapro-dev/BHVIVA.mp4",
    ####
    "DFGNT": "https://s3.us-east-1.wasabisys.com/mediapro-dev/DFGNT.mp4",
    "DFGNW": "https://s3.us-east-1.wasabisys.com/mediapro-dev/DFGNW.mp4",
    "DFSPO": "https://s3.us-east-1.wasabisys.com/mediapro-dev/DFSPO.mp4",
    "DFMSW": "https://s3.us-east-1.wasabisys.com/mediapro-dev/DFMSW.mp4",
    "DFVIVA": "https://s3.us-east-1.wasabisys.com/mediapro-dev/DFVIVA.mp4",
    ####
    "RS1GNT": "https://s3.us-east-1.wasabisys.com/mediapro-dev/RS1GNT.mp4",
    "RS1GNW": "https://s3.us-east-1.wasabisys.com/mediapro-dev/RS1GNW.mp4",
    "RS1SPO": "https://s3.us-east-1.wasabisys.com/mediapro-dev/RS1SPO.mp4",
    "RS1MSW": "https://s3.us-east-1.wasabisys.com/mediapro-dev/RS1MSW.mp4",
    "RS1VIVA": "https://s3.us-east-1.wasabisys.com/mediapro-dev/RS1VIVA.mp4",
    ####
    "SP1GNT": "https://s3.us-east-1.wasabisys.com/mediapro-dev/SP1GNT.mp4",
    "SP1GNW": "https://s3.us-east-1.wasabisys.com/mediapro-dev/SP1GNW.mp4",
    "SP1SPO": "https://s3.us-east-1.wasabisys.com/mediapro-dev/SP1SPO.mp4",
    "SP1MSW": "https://s3.us-east-1.wasabisys.com/mediapro-dev/SP1MSW.mp4",
    "SP1VIVA": "https://s3.us-east-1.wasabisys.com/mediapro-dev/SP1VIVA.mp4",
    ####
    "CE1GNT": "https://s3.us-east-1.wasabisys.com/mediapro-dev/CE1GNT.mp4",
    "CE1GNW": "https://s3.us-east-1.wasabisys.com/mediapro-dev/CE1GNW.mp4",
    "CE1SPO": "https://s3.us-east-1.wasabisys.com/mediapro-dev/CE1SPO.mp4",
    "CE1MSW": "https://s3.us-east-1.wasabisys.com/mediapro-dev/CE1MSW.mp4",
    "CE1VIVA": "https://s3.us-east-1.wasabisys.com/mediapro-dev/CE1VIVA.mp4",
    
    "CURGNT": "https://s3.us-east-1.wasabisys.com/mediapro-dev/CURGNT.mp4",
    "CURGNW": "https://s3.us-east-1.wasabisys.com/mediapro-dev/CURGNW.mp4",
    "CURSPO": "https://s3.us-east-1.wasabisys.com/mediapro-dev/CURSPO.mp4",
    "CURMSW": "https://s3.us-east-1.wasabisys.com/mediapro-dev/CURMSW.mp4",
    

    "CAMGNT": "https://s3.us-east-1.wasabisys.com/mediapro-dev/CAMGNT.mp4",
    "CAMGNW": "https://s3.us-east-1.wasabisys.com/mediapro-dev/CAMGNW.mp4",
    "CAMSPO": "https://s3.us-east-1.wasabisys.com/mediapro-dev/CAMSPO.mp4",
    "CAMMSW": "https://s3.us-east-1.wasabisys.com/mediapro-dev/CAMMSW.mp4",
    "CAMVIVA": "https://s3.us-east-1.wasabisys.com/mediapro-dev/CAMVIVA.mp4",

    "PE1GNT": "https://s3.us-east-1.wasabisys.com/mediapro-dev/PE1GNT.mp4",
    "PE1GNW": "https://s3.us-east-1.wasabisys.com/mediapro-dev/PE1GNW.mp4",
    "PE1SPO": "https://s3.us-east-1.wasabisys.com/mediapro-dev/PE1SPO.mp4",
    "PE1MSW": "https://s3.us-east-1.wasabisys.com/mediapro-dev/PE1MSW.mp4",
    "PE1VIVA": "https://s3.us-east-1.wasabisys.com/mediapro-dev/PE1VIVA.mp4",
    
}

# A frase que estamos procurando
target_phrase = "Sinal não encontrado"

def log_message(message):
    chamar(message)


def check_video_for_phrase_and_consistency(video_key, video_url, target_phrase):
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
        text = pytesseract.image_to_string(gray, lang='por')
        # Verificar se a frase está no texto reconhecido
        if target_phrase in text:
            #log_message(f"Possível problema no vídeo {video_key}, {video_url}")
            #log_message(f"Realizando sintonia")
            #obter(video_key[:2], channel )    
            error_vids('Sem sinal no video', video, video_url, channel, video_key, blue=False)
            cap.release()
            return True
          # Retornar para garantir que o loop principal continue
        #similar_thumbs = check_frame_repetition(video_url)
        #if similar_thumbs == True:
            ##log_message(f"Video Travado {video_url} ") 
            #error_vids('Video Travado', video, video_url, channel)
           # cap.release()
           # return True  # Retornar para garantir que o loop principal continue
            
    cap.release()
    validation_result = process_video(video_url)
    validation_blue = process_video_blue(video_url)
    if validation_result == True and validation_blue == False:
        print('1')
        error_vids('Tela Travada', video, video_url, channel, video_key, blue = False)
    if validation_result == True and validation_blue == True:
        print('2')
        error_vids('Decoder Desligado', video, video_url, channel, video_key, blue=True)
    else:
         print(validation_result)

    
    
    return False  # Se não encontrou problemas, retornar False


def error_vids(error, key, video, channel, video_key, blue): # Deve consertar o erro de não achar o similares
    print(blue)
    time.sleep(5)
    if blue == False:
        print('False blue')
        if video_key[:3] in ['CUR', 'CAM']:
                log_message(f'{error} {video}')
                obter(video_key[:3], video_key[2:].lower())
                print(video_key[:3], video_key[2:].lower())
        else:
                log_message(f'{error} {video}')
                obter(key, channel)
    else:
        print('True blue')
        if video_key[:3] in ['CUR', 'CAM']:
            log_message(f'{error} {video}')
            received(video_key[:3], video_key[2:].lower())
        else:
            log_message(f'{error} {video}')
            received(key, channel)

def main():
    while True:  # Loop infinito para rodar indefinidamente
        for video_key, video_url in video_urls.items():
            # Verificar o vídeo diretamente da URL
            found = check_video_for_phrase_and_consistency(video_key, video_url, target_phrase)
            print(found)

            if not found:
                print(f"Frase não encontrada no vídeo {video_key}")
        # Pausar por 30 minutos (1800 segundos) antes de analisar novamente
        print("Aguardando 30 minutos antes da próxima análise...")
        time.sleep(3600)

if __name__ == "__main__":
    main()

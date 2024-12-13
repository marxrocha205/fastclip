import cv2
import numpy as np

def get_color_name(hsv_pixel):
    h, s, v = hsv_pixel[0], hsv_pixel[1], hsv_pixel[2]
    
    # Define faixas para diferentes cores no espaço HSV
    if h < 10 or h > 160:
        return 'Red'
    elif 10 < h < 30:
        return 'Orange'
    elif 30 < h < 50:
        return 'Yellow'
    elif 50 < h < 80:
        return 'Green'
    elif 80 < h < 130:
        return 'Blue'
    elif 130 < h < 160:
        return 'Purple'
    else:
        return 'Unknown'

def detect_colors_in_frame(frame):
    # Converter para HSV para facilitar a detecção de cores
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Definir um dicionário para contar a ocorrência das cores
    color_counts = {
        'Red': 0,
        'Orange': 0,
        'Yellow': 0,
        'Green': 0,
        'Blue': 0,
        'Purple': 0
    }
    
    # Verificar a cor de cada pixel
    for row in hsv_frame:
        for pixel in row:
            color_name = get_color_name(pixel)
            if color_name in color_counts:
                color_counts[color_name] += 1
    
    # Retornar as cores detectadas no frame
    return color_counts

def detect_colors_in_video(video_path):
    # Abrir o vídeo
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return
    
    # Inicializar um dicionário para contar as cores ao longo de todo o vídeo
    total_color_counts = {
        'Red': 0,
        'Orange': 0,
        'Yellow': 0,
        'Green': 0,
        'Blue': 0,
        'Purple': 0
    }
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # Detectar as cores no frame
        frame_color_counts = detect_colors_in_frame(frame)
        
        # Acumular as contagens de cores do frame no total
        for color, count in frame_color_counts.items():
            total_color_counts[color] += count
    
    cap.release()
    
    # Imprimir as cores detectadas no vídeo
    for color, count in total_color_counts.items():
        if count > 0:
            print(f"A cor {color} apareceu {count} vezes no vídeo.")

# Exemplo de uso
video_path = 'BHSPO.mp4'  # Substitua pelo caminho do seu vídeo
detect_colors_in_video(video_path)

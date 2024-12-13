import cv2
import numpy as np


def frames_are_equal(frame1, frame2, threshold=0.01):
    # Converta os frames para escala de cinza
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    # Calcule a diferença absoluta entre os frames
    difference = cv2.absdiff(gray1, gray2)
    
    # Calcule o número de pixels que são diferentes
    non_zero_count = np.count_nonzero(difference)
    
    # Verifique se a diferença é menor do que o limiar
    return non_zero_count / (gray1.size) < threshold

def check_frame_repetition(video_path):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return False  # Retornar False se não puder abrir o vídeo

    prev_frame = None
    frame_index = 0
    repetitions = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if prev_frame is not None:
            if frames_are_equal(prev_frame, frame):
                repetitions.append(frame_index)
        prev_frame = frame
        frame_index += 1
    cap.release()
    # Se houver repetições de frames, retornar True
    if repetitions:
       print('True')
       return True
    else:
       print('False')
       return False
import subprocess
import os
import glob
import time 

def get_video_duration(video_url):
    """Obtém a duração do vídeo usando ffprobe."""
    cmd = [
        "ffprobe", "-v", "quiet", "-show_entries", "format=duration", 
        "-of", "csv=p=0", video_url
    ]
    
    # Executa o comando e captura a saída
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Converte a saída para string e remove espaços extras
    duration = result.stdout.decode("utf-8").strip()
    
    return float(duration)

def calculate_fps(duration, num_images=10):
    """Calcula o FPS com base na duração do vídeo e no número desejado de imagens."""
    fps = num_images / duration
    return round(fps, 2)

def extract_frames(video_url, fps):
    """Extrai os frames do vídeo usando o ffmpeg e retorna os arquivos criados."""
    cmd = [
        "ffmpeg", "-y", "-i", video_url, "-r", str(fps), "%02d.png"
    ]
    subprocess.run(cmd)
    
    # Retorna a lista de arquivos PNG criados
    return glob.glob("*.png")

def cleanup_images(image_files):
    """Apaga as imagens criadas após a execução."""
    for image in image_files:
        os.remove(image)

def compare_images():
    """Compara as imagens PNG usando o comando ffmpeg e retorna o número de comparações > 0.9."""
    cmd = (
        'ffmpeg -y -i 01.png -i 02.png -i 03.png -i 04.png -i 05.png -i 06.png '
        '-i 07.png -i 08.png -i 09.png -i 10.png '
        '-lavfi "[0:v][1:v]ssim;[1:v][2:v]ssim;[2:v][3:v]ssim;[3:v][4:v]ssim;'
        '[4:v][5:v]ssim;[5:v][6:v]ssim;[6:v][7:v]ssim;[7:v][8:v]ssim;[8:v][9:v]ssim;'
        '[9:v][0:v]ssim" -f null - 2>&1 | grep Parsed_ssim | sort -n -k1,1 | '
        'awk \'{print $11}\' | tr -d "All:" | awk \'$1>0.9{c++} END{print c+0}\''
    )
    
    # Executa o comando
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Captura a saída e converte para número inteiro
    comparison_count = int(result.stdout.decode("utf-8").strip())
    
    return comparison_count

def process_video(video_url):
    """Função principal que será chamada de outro script."""
    # Obtém a duração do vídeo
    duration = get_video_duration(video_url)
    
    # Calcula o FPS para gerar 10 imagens
    fps = calculate_fps(duration)
    
    # Extrai os frames do vídeo
    image_files = extract_frames(video_url, fps)
    
    # Realiza a comparação das imagens
    comparison_result = compare_images()
    time.sleep(2)
    # Limpa os arquivos gerados após a extração
    cleanup_images(image_files)
    
    # Verifica o resultado e imprime True ou False
    if comparison_result > 5:
        print("True")
        return True
    else:
        print("False")
        return False


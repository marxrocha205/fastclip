import subprocess
import os
import requests

def download_video(url, output_path):
    """Baixa o vídeo do URL para o caminho especificado."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Verifica se o download foi bem-sucedido

        # Salva o arquivo baixado
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Download do vídeo concluído: {output_path}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o vídeo: {e}")
        return False
    return True

def process_video_blue(video_url):
    # Caminho temporário para salvar o vídeo baixado
    downloaded_video = 'temp_video.mp4'
    
    # Baixa o vídeo
    if not download_video(video_url, downloaded_video):
        return

    # Define o nome de saída do vídeo processado
    output_video = 'out.mp4'

    # Comando FFmpeg para cortar o vídeo
    ffmpeg_command = [
        'ffmpeg', '-y', '-hide_banner', '-loglevel', 'error',
        '-i', downloaded_video, '-vf', 'crop=200:200', output_video
    ]

    # Executa o FFmpeg para processar o vídeo
    try:
        subprocess.run(ffmpeg_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao processar o vídeo: {e}")
        return

    # Comando FFprobe para calcular HUEAVG
    ffprobe_command = [
        'ffprobe', '-f', 'lavfi', 'movie=out.mp4,signalstats',
        '-show_entries', 'frame_tags=lavfi.signalstats.HUEAVG',
        '-of', 'flat'
    ]

    try:
        # Executa o ffprobe e captura a saída
        result = subprocess.run(ffprobe_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout

        # Filtra e processa a saída para obter os valores de HUEAVG
        hue_values = []
        for line in output.splitlines():
            if 'frames.frame' in line:
                value = line.split('"')[1]  # Extrai o valor numérico
                hue_values.append(float(value))

        # Calcula o máximo e o mínimo dos valores
        if hue_values:
            max_hue = max(hue_values)
            min_hue = min(hue_values)

            # Verifica a condição para determinar se o vídeo é "azul" ou "ok"
            if max_hue - min_hue < 1 and 290 < max_hue < 310:
                return True
            else:
                return False
        else:
            print("Nenhum valor HUEAVG encontrado.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o ffprobe: {e}")

    # Apaga o vídeo de saída após o processamento
    if os.path.exists(output_video):
        try:
            os.remove(output_video)
            print(f"Vídeo {output_video} removido com sucesso.")
        except OSError as e:
            print(f"Erro ao remover o vídeo {output_video}: {e}")

    # Remove o vídeo baixado temporariamente
    if os.path.exists(downloaded_video):
        try:
            os.remove(downloaded_video)
            print(f"Vídeo baixado {downloaded_video} removido com sucesso.")
        except OSError as e:
            print(f"Erro ao remover o vídeo baixado {downloaded_video}: {e}")

# Exemplo de uso


import paramiko
from telegram import *

# Dicionário com as informações dos IPs e portas
ips_dict = {
    'BH': {'porta': 2222, 'ip': '177.128.26.59'},
    'SP': {'porta': 2224, 'ip': '201.6.108.229'},
    'DF': {'porta': 2223, 'ip': '189.6.79.32'},
    'RS': {'porta': 2525, 'ip': '189.112.176.189'},
    'CE': {'porta': 2222, 'ip': '187.18.155.239'},
    'PE': {'porta': 51022, 'ip': '190.89.34.230'},
    'CUR': {'porta': 4221, 'ip': '179.184.26.136'},
}

def listar():
    """Lista todos os IPs e portas do dicionário."""
    for nome, info in ips_dict.items():
        porta = info['porta']
        ip = info['ip']
        print(f'{nome}, {porta}, {ip}')

def obter(sigla, rest):
    """Obtém e conecta ao IP e porta correspondentes à sigla fornecida."""
    info = ips_dict.get(sigla)
    if info:
        print(f"IP: {info['ip']}, Porta: {info['porta']}")
        ip = info['ip']
        porta = info['porta']
        if sigla in ['SP', 'CE','RS', 'PE']:
            rest = rest[1:].lower()
            print(1)
            connect(ip, porta, rest, sigla)
        elif sigla in ['CAM', 'CUR']:
            rest = rest[1:].lower()
            print(2)
            connect(ip, porta, rest, sigla)
        else:
            print(3)
            connect(ip, porta, rest, sigla)
        
    else:
        print(f"Sigla {sigla} não encontrada.")
        return None, None

def connect(ip, porta, rest, sigla):
    """Conecta ao servidor SSH usando o IP e porta fornecidos e executa o script ./spo.sh."""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=porta, username='tdsoft', password='C0p1@0')
        chamar(f'Connect : {sigla} Channel: {rest}')
        # Navega até o diretório /itach e executa o script ./spo.sh
        command = f"cd itach && ./{rest}.sh"
        stdin, stdout, stderr = ssh.exec_command(command)
        
        # Lê a saída e erros do comando
        print("Saída:")
        for line in stdout:
            print(line.strip())
        
        print("Erros:")
        for line in stderr:
            print(line.strip())
        
    except paramiko.SSHException as e:
        print(f"Erro ao conectar: {e}")
        chamar(f"Erro:{e}")
    finally:
        chamar('finalizado')
        ssh.close()

# Exemplo de uso
#listar()
#video_key = 'CURGNT'

#video = video_key[:3]
#channel = video_key[3:].lower()

#print(video, channel)
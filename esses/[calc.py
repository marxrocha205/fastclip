from datetime import timedelta
from datetime import timedelta

# Lista de tempos no formato "hora:minuto:segundo"
tempos = [
    "1:25:00", "1:00:00", "1:25:00", "1:59:00", "1:25:00", "1:59:00", 
    "1:25:00", "1:59:00", "1:25:00", "0:47:00", "1:25:00", "0:54:00", 
    "1:59:00", "1:00:00", "1:25:00", "1:35:00", "1:25:00", "0:45:00", 
    "1:25:00", "1:20:00", "1:25:00", "1:55:00", "1:25:00", "1:20:00", 
    "1:25:00", "0:59:00", "1:25:00", "1:00:00", "1:25:00", "1:59:00"
]

# Inicializa a variável para armazenar o total de tempo
tempo_total = timedelta()

# Converte cada tempo para timedelta e adiciona ao tempo total
for tempo in tempos:
    horas, minutos, segundos = map(int, tempo.split(':'))
    tempo_total += timedelta(hours=horas, minutes=minutos, seconds=segundos)

# Converte o total de segundos para dias
dias_totais = tempo_total.total_seconds() / (24 * 3600)

# Arredonda o valor para o número inteiro mais próximo
dias_totais_arredondados = round(dias_totais)

# Exibe o resultado arredondado
print(f"Tempo total em dias: {dias_totais_arredondados}")
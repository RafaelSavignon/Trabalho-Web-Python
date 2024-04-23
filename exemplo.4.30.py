import datetime

dataNascimento = datetime.datetime(2002, 1, 8)
dataAtual = datetime.datetime.now()

diferenca = dataAtual - dataNascimento

print(f"Você viveu {diferenca.days} dias")
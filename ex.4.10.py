import re

frase = input("Digite uma frase: ")
artigos = r'\b(o|a|os|as|um|uma|uns|umas)\b'
frase_sem_artigo = re.sub(artigos, "", frase)

print(frase_sem_artigo)
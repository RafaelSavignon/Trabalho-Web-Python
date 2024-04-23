frase = input("Digite uma frase: ")
resultado = frase.split()
contadorA = 0
contadorO = 0

for i in resultado:
    if i.endswith("a"):
        contadorA = contadorA + 1
    elif i.endswith("o"):
        contadorO = contadorO + 1

print(f"você digitou {contadorA} palavras que terminam em 'A' e {contadorO} palavras que terminam em 'O'")
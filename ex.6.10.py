frase = input("Digite uma frase: ")
lista_frase = frase.split()

comprimento = map(lambda x: len(x), lista_frase)
print(list(comprimento))
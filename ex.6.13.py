lista1 = [2, 4, 6, 8, 10]
lista2 = [12, 14, 16, 18, 20]

resultado = zip(lista1, lista2)
medias = [(n1 + n2)/2 for n1, n2 in resultado]
print(list(medias))
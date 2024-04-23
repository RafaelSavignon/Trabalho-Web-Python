from typing import List


def adicionar(lista: List[int], novo_elemento: int):
    lista.append(novo_elemento)

idades = [21, 18, 17, 22, 19]
adicionar(idades, 25)
print(idades)
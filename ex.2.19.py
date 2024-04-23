import random

sorteio = random.randint(1, 10)

palpite = int(input("Digite um palpite: "))

if palpite == sorteio:
    print(f"Acertou!")
elif palpite < sorteio:
    print(f"Chutou baixo")
else:
    print(f"Chutou alto")
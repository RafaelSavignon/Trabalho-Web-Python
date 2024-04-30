import random


opcoes = ["pedra", "papel", "tesoura"]
npc = random.choice(opcoes)
print("Suas opções:")
print("1 - pedra")
print("2 - papel")
print("3 - tesoura")
usuario = int(input("Qual sua escolha?: "))
op_usuario = opcoes[usuario - 1]

if npc == op_usuario:
    print("empatou")
if npc == "pedra" and op_usuario == "tesoura":
    print(f"Computador venceu com '{npc}' contra '{op_usuario}'")
elif npc == "pedra" and op_usuario == "papel":
    print(f"Usuario venceu com '{op_usuario}' contra '{npc}'")

if npc == "papel" and op_usuario == "pedra":
    print(f"Computador venceu com '{npc}' contra '{op_usuario}'")
elif npc == "papel" and op_usuario == "tesoura":
    print(f"Usuario venceu com '{op_usuario}' contra '{npc}'")

if npc == "tesoura" and op_usuario == "papel":
    print(f"Computador venceu com '{npc}' contra '{op_usuario}'")
elif npc == "tesoura" and op_usuario == "pedra":
    print(f"Usuario venceu com '{op_usuario}' contra '{npc}'")
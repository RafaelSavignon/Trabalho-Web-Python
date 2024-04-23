import re

usuario = input("Digite um nome de usuario: ")
senha = input("Digite uma senha: ")

usuario_processado = re.sub(r"\W", "", usuario)
senha_processado = re.sub(r"\W", "", senha)

print(usuario_processado)
print(senha_processado)
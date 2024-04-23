letra = input("Digite uma letra: ")
vogal = ["a", "e", "i", "o", "u"]

if letra in vogal:
    print(f"a letra {letra} é uma vogal")
else:
    print(f"a letra {letra} é uma consoante")
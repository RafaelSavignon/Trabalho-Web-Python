while True:
    frase = input("Digite uma frase com 5 palavras: ")
    resultado = frase.split()
    tamanho = len(resultado)

    if tamanho != 5:
        frase = input("Digite novamente, a frase precisa ter 5 palavras: ")
        resultado = frase.split()

    for i in resultado:
        print(i)
    break

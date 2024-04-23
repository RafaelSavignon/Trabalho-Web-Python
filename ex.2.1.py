numero1 = int(input("Digite o primeiro numero: "))
eh_par = (numero1 % 2 == 0)

if eh_par:
    print(f"p numero {numero1} é par")
else:
    print(f"o numero {numero1} é impar")
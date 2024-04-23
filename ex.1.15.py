valor = float(input("Digite o valor da venda: "))
desconto = float(input("Digite o percentual de desconto: "))
imposto = float(input("Digite o percentual de imposto: "))

valor_descontado = valor - (valor * (desconto/100))
valor_final = valor_descontado - (valor_descontado * (imposto/100))



print(f"o lucro total é de R$ {valor_final:.2f} e o valor com desconto é de R$ {valor_descontado:.2f}")
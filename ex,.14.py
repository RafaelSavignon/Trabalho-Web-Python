nome = input("Digite o nome do produto: ")
preco_custo = float(input("Digite o preço do produto: "))
preco_venda = float(input("Digite o preço de venda do produto: "))
qtd = int(input("Digite a quantidade do produto: "))

lucro_por_produto = preco_venda - preco_custo
lucro_total = qtd * lucro_por_produto



print(f"o lucro total é de R$ {lucro_total:.2f}")
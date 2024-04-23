vinhos = {"A": 35, "B": 55, "C": 45, "D": 65, "E": 75}
filtro = lambda v : v > 50
vinhos_caros = list(filter(filtro, vinhos.values()))
print(vinhos_caros)
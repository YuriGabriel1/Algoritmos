Distancia = float(input("Informe a distância que pretende percorrer: "))

if Distancia <= 200:
    preco = Distancia * 0.50
else:
    preco = Distancia * 0.45

print(f"O preço da passagem ficou R${preco:.2f}")

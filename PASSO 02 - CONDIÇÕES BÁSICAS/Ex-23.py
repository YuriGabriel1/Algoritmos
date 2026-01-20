nome = input("Informe seu nome:")
genero = input("Você e do Genêro masculino ou femino? (M/F):").lower()
produto = float(input("Informe o preço do produto:"))
if genero == "m":
    desconto = produto * 0.05
    preco_final =  produto - desconto
    print(f"O senhor {nome} recebeu 5% de desconto.")
    print(f"Valor do desconto: R$ {desconto:.2f}")
    print(f"Preço final: R$ {preco_final:.2f}")

elif genero == "f":
    desconto = produto * 0.13
    desconto = produto * 0.13
    preco_final = produto - desconto
    print(f"A senhora {nome} recebeu 13% de desconto.")
    print(f"Valor do desconto: R$ {desconto:.2f}")
    print(f"Preço final: R$ {preco_final:.2f}")
else:
    print("Gênero inválido. Digite M ou F")

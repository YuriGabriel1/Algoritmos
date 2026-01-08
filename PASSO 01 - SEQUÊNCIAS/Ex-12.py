
preco = float(input("Digite o preço do produto: R$ "))

desconto = preco * 0.05
preco_promocional = preco - desconto

print(f"Preço original: R$ {preco:.2f}")
print(f"Preço promocional com 5% de desconto: R$ {preco_promocional:.2f}")

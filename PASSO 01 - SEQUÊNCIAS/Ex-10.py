largura = float(input("Digite a largura da parede (em metros): "))
altura = float(input("Digite a altura da parede (em metros): "))

area = largura * altura
tinta = area / 2

print(f"Área a ser pintada: {area:.2f} m²")
print(f"Quantidade de tinta necessária: {tinta:.2f} litros")

salario = float(input("Informe seu salário:"))
casa = float(input("Informe o valor da casa:"))
anos= int(input("Quantos  anos  ira ficar na casa?:"))
meses = anos *12
valor_mensal = casa/meses
limite = salario * 0.30
print("__"*30)
print(f"Prestação:R$ {valor_mensal:.2f}")
print(f"Limite de 30% do salário:R$ {limite:.2f}")
print("__"*30)
if valor_mensal > limite:
    print("O emprestimo não foi aprovado excede 30% do seu salário!")
else:
    print("Foi aprovado pode ficar com o emprestimo")
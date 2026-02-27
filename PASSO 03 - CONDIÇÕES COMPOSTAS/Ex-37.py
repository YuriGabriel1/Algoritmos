salario = float(input("Informe seu salário: "))
anos = int(input("Quantos anos trabalha na empresa: "))
genero = input("Informe o seu gênero Feminino ou masculino (F/M): ").lower()

if genero == "f":
    if anos < 15:
        aumento = salario * 0.05
    elif anos <= 20:
        aumento = salario * 0.12
    else:
        aumento = salario * 0.23

elif genero == "m":
    if anos < 20:
        aumento = salario * 0.03
    elif anos <= 30:
        aumento = salario * 0.13
    else:
        aumento = salario * 0.25

novo_salario = salario + aumento

print(f"Salário antigo: R${salario:.2f}")
print(f"Novo salário: R${novo_salario:.2f}")
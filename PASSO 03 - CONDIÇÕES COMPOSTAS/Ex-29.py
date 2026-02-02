nome = input("Nome do funcionario:")
salario = float(input("Informe o salário do funcionario:"))
anos = int(input("informe quantos anos o funcionario trabalha na empresa:"))

if anos <=3:
    novo_salario = salario * 1.03
    print(f"O salário de R${salario}, teve um reajuste de  3 anos R${novo_salario}")
    print(f"Do funcionario {nome}")
elif  anos <=10:
    novo_salario = salario * 1.125
    print(f"O salário de R${salario}, teve  um aumento entre 3 e 10 anos R${novo_salario}")
    print(f"Do funcionario {nome}")
else:
    novo_salario = salario * 1.20
    print(f"Você teve um aumente  de 20% pois vc esta a mais de 10 anos ou mais na empresa,o novo salário ficou de R${novo_salario} ")
    print(f"Do funcionario {nome}")
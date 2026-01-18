from datetime import  datetime
ano_nascimento = int(input("Informe o ano de nascimento"))
ano_atual =  datetime.now().year
idade =  ano_atual- ano_nascimento
tempo = idade - 18
if tempo > 0:
    print(f"Você já deveria ter se alistado há {tempo} anos")
elif tempo == 0:
    print(f"È hora de se alistar!")
else:
    print(f"Ainda Faltam {tempo} anos para o alistamento")
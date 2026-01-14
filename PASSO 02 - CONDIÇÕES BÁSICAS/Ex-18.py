from datetime import  datetime
ano = int(input("Digite o ano de nascimento: "))
atual = datetime.now().year
idade = atual - ano
if idade >= 18:
    print("Você já pode vota!")
else:
    print("Você não tem idade para voto")

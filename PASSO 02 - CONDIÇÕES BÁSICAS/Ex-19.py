from time import sleep
nome= str(input("Digite seu nome: "))
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2 )/2
print("Sua nota sera calculada!")
sleep(1)
if media >= 7:
    print("Você teve um bom aproveitamento!")
    sleep(1)
    print(f"O aluno {nome} com a média de {media} ")
else:
    print(f"O aluno {nome} Você não teve um bom aproveitamento com a média de {media}")


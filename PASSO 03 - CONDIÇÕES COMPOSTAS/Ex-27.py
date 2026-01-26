from time import sleep
nota1 = float(input("Informe a primeira nota:"))
sleep(1)
nota2 = float(input("Informe a segunda nota:"))
sleep(1)
media = (nota1 + nota2)/2
if 5.0 <= media <= 6.9:
    print("Recuperação!")
elif media <=4.9:
    print("Reprovado")
elif media >=7:
    print("Aprovado")

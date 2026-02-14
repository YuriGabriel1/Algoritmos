import random

while True:
    computador = random.randint(1, 5)
    jogador = int(input("Tente adivinhar  o número sorteado pelo computador entre 1 a 5:"))
    if jogador == computador:
        print(f"Você  acertou o número do computador foi:{computador}")
        continuar = input("deseja continuar? sim/nao:").lower()
        if continuar == "nao" or continuar == "n" or continuar == "não":
            print("jogo finalizado")
            break
    else:
        print(f"Você errou o número do computador era {computador}")
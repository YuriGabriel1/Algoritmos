import random

print("=== JOKENPÔ ===")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

jogador = int(input("Escolha uma opção: "))

computador = random.randint(1, 3)

if computador == 1:
    print("Computador escolheu Pedra")
    print(f"Jogador escolheu {jogador}")
elif computador == 2:
    print("Computador escolheu Papel")
    print(f"Jogador escolheu {jogador}")
else:
    print("Computador escolheu Tesoura")
    print(f"Jogador escolheu {jogador}")
if jogador == computador:
    print(f"O computador escolheu o mesmo do jogador{computador}")
    print(f"Jogador escolheu {jogador}")
    print("Empate!")
elif (jogador == 1 and computador == 3) or \
     (jogador == 2 and computador == 1) or \
     (jogador == 3 and computador == 2):
    print("Você ganhou! ")

else:
    print("Computador ganhou!")
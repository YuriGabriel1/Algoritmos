from time import sleep
print("__"*30)
print("Escolha umas das opções abaixo para alugar o carro, P para carro popular e L para carro de Luxo")
print("__"*30)
carro = input("Opções (P/L):").lower()
print("__"*30)
sleep(1)
print("__"*30)
dias = int(input("Quantos dias vai alugar o carro?:"))
km = float(input("Quantos km foram percorridos?:"))
print("__"*30)
if carro == "p":
    print("Você escolheu carro popular ou seja  o aluguel é de R$90 reais  por dia ")
    if km <= 100:
        total = (90 * dias) + (0.20 * km)
        print(f"O preço a ser pago será de R${total}")
    elif km > 100:
        total = (90 * dias) + (0.20 * 100) + (0.10*(km-100))
        print(f"O preço a ser pago será de R${total}")
elif carro == "l":
    print("Você escolheu carro de luxo  ou seja  o aluguel é de R$150 reais  por dia ")
    if km <= 200:
        total = (150 * dias) + (0.30 * km)
        print(f"O preço a ser pago será de R${total}")
    else:
        total = (150 * dias) + (0.30 * 200) + (0.25 * (km - 200))
        print(f"O preço a ser pago será de R${total}")
else:
    print("opção invalida! tente novamente escolhendo  carro de luxo ou carro popular!")
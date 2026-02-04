a = float(input("Digite o primeiro lado:"))
b = float(input("Digite o segundo lado:"))
c = float(input("Digite o terceiro lado:"))
if (a < b + c) and (b < a + c) and (c < a + b):
    print("É possível formar um triângulo")

    if (a == b) and (b == c):
        print("Triângulo EQUILÁTERO (todos os lados iguais)")

    elif (a == b) or (a == c) or (b == c):
        print("Triângulo ISÓSCELES (dois lados iguais)")

    else:
        print("Triângulo ESCALENO (todos os lados diferentes)")
else:
    print("Não é possível formar um triângulo")
a = float(input("Digite o comprimento do primeiro segmento: "))
b = float(input("Digite o comprimento do segundo segmento: "))
c = float(input("Digite o comprimento do terceiro segmento: "))
if a < b + c and b < a + c and c < a + b:
    print("É possível formar um triângulo com esses segmentos.")
else:
    print("Não é possível formar um triângulo com esses segmentos.")

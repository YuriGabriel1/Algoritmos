peso = float(input("Informe seu peso:"))
altura = float(input("Qual a sua altura?:"))
imc = peso / (altura*altura)

if imc < 18.5:
    print("Seu peso esta baixo!")
elif  18.5 <= imc < 25:
    print("Peso ideal")
elif 25 <= imc < 30:
    print("Esta acima do peso ideal")
elif 30 <= imc < 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")
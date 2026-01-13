velocidade = int(input("Qual é a sua velocidade? km/h:"))
if velocidade > 80:
    print("Você foi multado!")
    multa =  velocidade- 80
    multa = multa *  5
    print(f"Sua multa foi de R${multa} reais")
else:
    print("Pode passar, você está no limite correto!")
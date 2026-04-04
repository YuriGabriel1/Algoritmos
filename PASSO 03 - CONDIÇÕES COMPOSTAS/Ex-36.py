horario = float(input("Quantas horas de atividade física você fez? "))

if horario <= 10:
    pontos = horario * 2
elif horario <= 20:
    pontos = horario * 5
else:
    pontos = horario * 10

dinheiro = pontos * 0.05

print(f"Pontos: {pontos}")
print(f"Dinheiro ganho: R${dinheiro:.2f}")

km_percorridos = float(input("Informe a quantidade de Km percorridos: "))
dias_alugados = int(input("Informe a quantidade de dias alugados: "))
preco_por_dia = 90.0
preco_por_km = 0.20
total_pagar = (dias_alugados * preco_por_dia) + (km_percorridos * preco_por_km)
print(f"O valor total a pagar é: R$ {total_pagar:.2f}")

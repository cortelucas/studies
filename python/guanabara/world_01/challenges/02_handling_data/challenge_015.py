# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por KM rodado.

print("----- Desafio 15 -----")

kms_traveled: float = float(input("Digite quantos KMs você percorreu: "))
days_traveled: int = int(input("Digite quantos dias você percorreu: "))
value_per_day: float = 60
value_per_km: float = 0.15

amount_payable: float = (days_traveled * value_per_day) + (kms_traveled * value_per_km)

print(f"O valor a pagar é R$ {amount_payable:.2f}")

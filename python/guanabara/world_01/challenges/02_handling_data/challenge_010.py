# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

print("----- Desafio 10 -----")

money: float = float(input("Digite quanto dinheiro você tem na carteira: R$ "))

print(f"Você pode comprar $ {money / 3.27:.2f}.")

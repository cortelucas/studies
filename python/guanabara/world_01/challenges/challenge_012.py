# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print("----- Desafio 12 -----")

price: float = float(input("Digite o preço do produto: R$ "))
discount: float = price * 0.05

print(
    f"O produto custava R$ {price:.2f} e com 5% de desconto ficou R$ {price - discount:.2f}"
)

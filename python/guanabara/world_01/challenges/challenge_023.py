""" 
  Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
  Ex: Digite um número: 1834
  Unidade: 4
  Dezena: 3
  Centena: 8
  Milhar: 1
"""

number: int = int(input("Digite um número de 0 a 9999: "))

unidade: int = number // 1 % 10
dezena: int = number // 10 % 10
centena: int = number // 100 % 10
milhar: int = number // 1000 % 10

print(
    f"Unidade: {unidade}"
    f"\nDezena: {dezena}"
    f"\nCentena: {centena}"
    f"\nMilhar: {milhar}"
)

"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

number_01: int = int(input("Digite o primeiro número: "))
number_02: int = int(input("Digite o segundo número: "))
number_03: int = int(input("Digite o terceiro número: "))

if number_01 > number_02 and number_01 > number_03:
    print(f"O maior número é {number_01}")
elif number_02 > number_01 and number_02 > number_03:
    print(f"O maior número é {number_02}")
else:
    print(f"O maior número é {number_03}")

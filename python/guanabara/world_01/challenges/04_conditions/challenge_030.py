"""
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

number: int = int(input("Digite um número inteiro: "))

if number % 2 == 0:
    print("O número é PAR!")
else:
    print("O número é ÍMPAR!")

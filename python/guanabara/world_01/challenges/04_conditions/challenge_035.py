"""
  Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""

reta_01: float = float(input("Digite o comprimento da primeira reta: "))
reta_02: float = float(input("Digite o comprimento da segunda reta: "))
reta_03: float = float(input("Digite o comprimento da terceira reta: "))

if (
    reta_01 < reta_02 + reta_03
    and reta_02 < reta_01 + reta_03
    and reta_03 < reta_01 + reta_02
):
    print("As retas podem formar um triângulo!")
else:
    print("As retas não podem formar um triângulo!")

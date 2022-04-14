# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

print("----- Desafio 05 -----")

number: int = int(input("Digite um número: "))
before: int = number - 1
after: int = number + 1

print(f"Antecessor: {before}"
      f"\nSucessor: {after}")
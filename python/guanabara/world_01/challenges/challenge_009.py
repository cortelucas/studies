# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

print("----- Desafio 09 -----")

number: int = int(input("Digite um número: "))


def multiplication_table(number: int) -> None:
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


multiplication_table(number)

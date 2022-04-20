"""
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint


random_number: int = randint(0, 5)
choice: int = int(input("Escolha um número de 0 a 5: "))

if choice == random_number:
    print("Você venceu!")
else:
    print(f"Você perdeu! o número era {random_number}")

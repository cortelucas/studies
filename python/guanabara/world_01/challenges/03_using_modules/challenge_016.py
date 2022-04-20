''' Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira '''

from math import trunc


number: float = float(input('Insira um número real: '))

print(f"O número {number} tem a parte inteira {trunc(number)}")

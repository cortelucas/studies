''' Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa '''

from math import hypot


cateto_adjacente: float = float(input('Insira o valor do cateto adjacente: '))
cateto_oposto: float = float(input('Insira o valor do cateto oposto: '))
hipotenusa: float = hypot(cateto_adjacente, cateto_oposto)

print(f'A hipotenusa do triângulo retângulo é {hipotenusa:.2f}')

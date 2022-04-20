''' Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo '''

from math import sin, cos, tan, radians


angle: float = float(input('Insira um ângulo: '))
sin: float = sin(radians(angle))
cos: float = cos(radians(angle))
tan: float = tan(radians(angle))

print(f'Seno: {sin:.2f}\nCosseno: {cos:.2f}\nTangente: {tan:.2f}')
'''
  Aula 08 - Módulos
'''


import math
import emoji
from random import randint


number: int = int(input('Insira um número: '))
sqrt: float = math.sqrt(number)

print(f'A raiz de {number} é {sqrt}!')

print(randint(1, 10))

print(emoji.emojize("Olá! :earth-americas:", use_aliases=True))

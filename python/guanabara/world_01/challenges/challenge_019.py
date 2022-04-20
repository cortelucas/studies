''' Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido. '''

from random import choice


alunos: list = ['Pedro', 'João', 'Maria', 'José']

print(f'O aluno sorteado foi {choice(alunos)}')

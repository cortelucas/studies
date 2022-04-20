''' O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. '''

from random import shuffle  


alunos: list = ['Pedro', 'João', 'Maria', 'José']
shuffle(alunos)
print(f'A ordem de apresentação será: {alunos}')
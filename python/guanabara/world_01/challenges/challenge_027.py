"""
  Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
  Ex: Ana Maria de Souza
  primeiro = Ana
  último = Souza
"""

name: str = input("Digite o nome completo: ")
first_name: str = name.split()[0]
last_name: str = name.split()[-1]

print(f"Primeiro nome: {first_name}" f"\nÚltimo nome: {last_name}")

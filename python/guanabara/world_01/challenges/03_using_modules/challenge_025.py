"""
  Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

name: str = input("Digite seu nome completo: ").strip()
have_silva: bool = "SILVA" in name.upper()

print(f"O nome {name} tem SILVA? {have_silva}")

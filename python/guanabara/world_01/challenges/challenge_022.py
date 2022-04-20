""" Crie um programa que leiao o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome
"""

name: str = input("Digite seu nome completo: ").strip()
upper: str = name.upper()
lower: str = name.lower()
qnt_letters: int = len(name) - name.count(" ")
qnt_first_name: int = name.find(" ")

print(
    f"Nome em maiúsculas: {upper}"
    f"\nNome em minúsculas: {lower}"
    f"\nQuantidade de letras: {qnt_letters}"
    f"\nQuantidade de letras do primeiro nome: {qnt_first_name}"
)

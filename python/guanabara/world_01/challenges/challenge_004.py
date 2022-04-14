# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

print("----- Desafio 04 -----")

any_data: str = input("Digite algo: ")

print(
    f"Alpha: {any_data.isalpha()}"
    f"\nNumber: {any_data.isnumeric()}"
    f"\nAlphanumeric: {any_data.isalnum()}"
    f"\nCapitalized: {any_data.istitle()}"
    f"\nLower: {any_data.islower()}"
    f"\nUpper: {any_data.isupper()}"
    f"\nAscii: {any_data.isascii()}"
    f"\nPrintable: {any_data.isprintable()}"
    f"\nSpace: {any_data.isspace()}"
)

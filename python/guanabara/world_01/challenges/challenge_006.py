# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

print("----- Desafio 06 -----")

number: int = int(input("Digite um número: "))
double: int = number * 2
triple: int = number * 3
sqrt: int | float = number ** (1/2)

print(f"Dobro: {double}"
      f"\nTriplo: {triple}"
      f"\nRaiz Quadrada: {sqrt:.2f}")

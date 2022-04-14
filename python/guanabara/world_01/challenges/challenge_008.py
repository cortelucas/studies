# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print("----- Desafio 08 -----")

meters: float = float(input("Digite um valor em metros: "))
centimeters: float = meters * 100
millimeters: float = meters * 1000

print(
    f"{meters}m em centímetros é {centimeters:.2f}cm"
    f"\n{meters}m em milímetros é {millimeters:.2f}mm"
)

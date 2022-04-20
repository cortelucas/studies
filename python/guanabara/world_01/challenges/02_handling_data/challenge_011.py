# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

print("----- Desafio 11 -----")

height: float = float(input("Digite a altura da parede: "))
width: float = float(input("Digite a largura da parede: "))

quantity_painting: float = height * width / 2

print(
    f"A área da sua parede é {height * width}m². A quantidade de tinta necessária para pintar a parede é de {quantity_painting:.2f} litros"
)

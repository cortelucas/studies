"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""

car_velocity: float = float(input("Digite a velocidade do carro: "))

if car_velocity > 80:
    print(f"Você foi multado! O valor da multa é de R${(car_velocity - 80) * 7:.2f}")
else:
    print("Você não foi multado!")

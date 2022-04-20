# Escreva um algoritmo que transforme graus Celsius em graus Fahrenheit.

print("----- Desafio 14 -----")

celsius: float = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit: float = ((celsius * 9) / 5) + 32

print(f"{celsius}°C em Fahrenheit é {fahrenheit:.2f}°F")

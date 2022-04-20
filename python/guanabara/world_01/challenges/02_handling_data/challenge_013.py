# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print("----- Desafio 13 -----")

salary: float = float(input("Digite o salário do funcionário: R$ "))
increase: float = salary * 0.15

print(
    f"O salário do funcionário era R$ {salary:.2f} e com 15% de aumento ficou R$ {salary + increase:.2f}"
)

"""
  Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""

salary: float = float(input("Digite o salário do funcionário: "))

if salary > 1250:
    salary_increase: float = salary * 0.10
    print(
        f"Aumento: R$ {salary_increase:.2f}"
        f"\nNovo Salário: R${salary + salary_increase:.2f}"
    )
else:
    salary_increase: float = salary * 0.15
    print(
        f"Aumento: R$ {salary_increase:.2f}"
        f"\nNovo Salário: R${salary + salary_increase:.2f}"
    )

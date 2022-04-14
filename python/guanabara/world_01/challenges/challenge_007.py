# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print("----- Desafio 07 -----")

grade_01: float = float(input("Digite a primeira nota: "))
grade_02: float = float(input("Digite a segunda nota: "))


def average(grade_01: float, grade_02: float) -> float:
    return (grade_01 + grade_02) / 2


print(f"Média: {average(grade_01, grade_02):.2f}")

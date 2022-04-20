"""
  Condições simples e compostas
"""

nota_01: float = float(input("Digite a nota 01: "))
nota_02: float = float(input("Digite a nota 02: "))
nota_03: float = float(input("Digite a nota 03: "))
nota_04: float = float(input("Digite a nota 04: "))

media: float = (nota_01 + nota_02 + nota_03 + nota_04) / 4

if media >= 6:
    print("Aprovado!")
elif media < 6 and media >= 4:
    print("Recuperação!")
else:
    print("Reprovado!")

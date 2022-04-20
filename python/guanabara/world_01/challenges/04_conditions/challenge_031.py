"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""

kms_travel: float = float(input("Digite a distância da viagem em Km: "))

if kms_travel <= 200:
    print(f"O valor da passagem é de R${kms_travel * 0.5:.2f}")
else:
    print(f"O valor da passagem é de R${kms_travel * 0.45:.2f}")

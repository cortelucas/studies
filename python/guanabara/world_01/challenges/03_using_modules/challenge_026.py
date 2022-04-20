"""
  Faça um programa que leia uma frase pelo teclado e mostre:
  - Quantas vezes aparece a letra "A".
  - Em que posição ela aparece a primeira vez.
  - Em que posição ela aparece a última vez.
"""

frase: str = input("Digite uma frase: ").strip()
frase_lower: str = frase.lower()
qnt_a: int = frase_lower.count("a")
first_position: int = frase_lower.find("a")
last_position: int = frase_lower.rfind("a")

print(
    f"A letra 'A' aparece {qnt_a} vezes na frase."
    f"\nA primeira vez que aparece é na posição {first_position}."
    f"\nA última vez que aparece é na posição {last_position}."
)

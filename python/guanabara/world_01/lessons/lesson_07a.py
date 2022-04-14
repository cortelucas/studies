"""
  Ordem de precedência

  1 - ()
  2 - **
  3 - * / // %
  4 - +
"""

number_01: int = int(input("Digite um número: "))
number_02: int = int(input("Digite outro número: "))

_sum: int = number_01 + number_02
_sub: int = number_01 - number_02
_mult: int = number_01 * number_02
_div: int | float = number_01 / number_02

print(f"Soma: {_sum}"
      f"\nSubtração: {_sub}"
      f"\nMultiplicação: {_mult}"
      f"\nDivisão: {_div}")

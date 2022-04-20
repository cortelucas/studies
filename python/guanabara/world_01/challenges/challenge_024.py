"""
  Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""

city_name: str = input("Digite o nome de uma cidade: ").strip()
city_name_upper: str = city_name.upper()
init_santo: bool = city_name_upper.startswith("SANTO")

print(f"A cidade {city_name} começa com SANTO? {init_santo}")

print("----- Desafio 03 -----")

number_01: int = int(input("Digite o primeiro número: "))
number_02: int = int(input("Digite o segundo número: "))


def sum(number_01: str, number_02: str) -> str:
    return str(number_01 + number_02)


print(f"A soma entre {number_01} e {number_02} é igual {sum(number_01, number_02)}")

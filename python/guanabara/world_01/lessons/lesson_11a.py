print("\033[0;30;40mOlá, Mundo!\033[m")

number_01: int = int(input("Digite um número inteiro: "))
number_02: int = int(input("Digite outro número inteiro: "))

print(
    f"A soma entre \033[32m{number_01}\033[m e \033[32m{number_02}\033[m é igual a \033[34m{number_01 + number_02}\033[m !"
)

colors: dict = {
    "black": "\033[0;30;40m",
    "red": "\033[0;31;40m",
    "green": "\033[0;32;40m",
    "yellow": "\033[0;33;40m",
    "blue": "\033[0;34;40m",
    "magenta": "\033[0;35;40m",
    "cyan": "\033[0;36;40m",
    "white": "\033[0;37;40m",
    "reset": "\033[0;0;0m",
}

print(
    f"A soma entre {colors['yellow']}{number_01}\033[m e {colors['magenta']}{number_02}\033[m é igual a {colors['blue']}{number_01 + number_02}\033[m !"
)

print(f"{colors['black']}Testando")

# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print("----- Desafio 08 -----")

meters: float = float(input("Digite um valor em metros: "))
quilometers: float = meters * 1000000
hectometers: float = meters * 100000
decameters: float = meters * 10000
decimeters: float = meters * 1000
centimeters: float = meters * 100
millimeters: float = meters * 1000

print(
    f"- {meters}m em quilometros é {quilometers:.2f}KM"
    f"\n- {meters}m em hectômetros é {hectometers:.2f}HM"
    f"\n- {meters}m em decâmetros é {decameters:.2f}DM"
    f"\n- {meters}m em decímetros é {decimeters:.2f}DM"
    f"\n- {meters}m em centímetros é {centimeters:.2f}cm"
    f"\n- {meters}m em milímetros é {millimeters:.2f}mm"
)

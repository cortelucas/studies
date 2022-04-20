frase: str = "Curso em Vídeo Python"
print(
    f"Capitalize: {frase.capitalize()}"
    f"\nTitle: {frase.title()}"
    f"\nUpper: {frase.upper()}"
    f"\nLower: {frase.lower()}"
    f"\nCount: {frase.count('o')}"
    f"\nCount: {frase.count('O')}"
    f"\nCount: {frase.count('o', 0, 13)}"
)

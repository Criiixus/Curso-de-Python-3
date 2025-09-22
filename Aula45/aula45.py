"""
Iteravel -> str, range, etc (__iter__)
Iterador -> quem sabe ebtreage um valor por vez
next -> mentregua o proximo valor
iter -> me entrega seu iterador
"""

texto = 'Cristian'
# iterador = iter(texto)

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)
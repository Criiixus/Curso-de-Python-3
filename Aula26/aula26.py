"""
Formatacao basica de string
s - string
d - int
f - float
.<numero de digito>f
x ou X - hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.783687368325:0=+10.1f}')
print(f'O hexadecimal de 1500 e {1500:08x}')
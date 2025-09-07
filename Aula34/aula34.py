"""
while (enquanto)
Executa uma acao enquanto um condicao for verdadeira
Loop infinito -> Quando um codigo nao tem fime 

"""

condicao = True 

while condicao:
    nome = input('Digite seu nome: ')
    print(f'Seu nome e {nome}')

    if nome == 'sair':
        break

print('Acabou')
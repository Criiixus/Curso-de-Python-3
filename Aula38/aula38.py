"""

Repeticoes 
While(enquanto)
Executa uma acao enqaunto uma condicao for verdadeira
Loop infinito -> Quando um codigo nao tem fim
"""
qtd_linha = 5
qtd_coluna = 6

linha = 1
while linha <= 5:
    coluna = 1
    while coluna <= qtd_coluna:
        print(f'{linha=} {coluna=}')
        coluna += 1 
    linha += 1

print('Acabou')

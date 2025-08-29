# 01234567
# Cristian
#-87654321



nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if "" in nome and idade:
    print(f"Seu nome e", nome)
    print(f"Seu nome invertido e",(nome[::-1]))

    if " " in nome:
        print('Seu nome contem Espaco')
    
    else:
        print(f'Seu nome nao tem espaco')

    print(f'Seu nome tem',len(nome[-0:8]),'Letras')

    print(f'A primeira letra do seu nome e',nome[-0:1])

    print(f'A ultima letra do seu nome e',nome[7:8])

else:
    print(f'Desculpe, voce deixou campos vazios')
    




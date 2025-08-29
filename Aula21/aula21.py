
# operadorws logicos
# and (e) or (ou) not (nao)
# and - Todas as condicoes precisam ser
# verdadeiras
# Se qualquer valor for consdierado falso,
# a expressao inteira sera avaliada naquele valor
# Sao consideradas falsy (que vc ja viu)
# 0 0.0 '' False
# Tambem eciste o tipo None que e
# usado para apresentar um nao valor

entrada = input('[E]ntrar [S]air')
senha_digitada = input("Senha:")    

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entra')
    
else:
    print('Sair')



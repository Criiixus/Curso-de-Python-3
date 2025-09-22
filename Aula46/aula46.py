for i in range(10):
    if i == 2:
        print('i e 2, pulando...')
        continue

    if i == 8:
        print('I igual a 8, else nao sera exucatado')
        break

    for j in range(1,3):
        print(i, j)
else:
    print('Fpor completo com sucesso')
nome = "Cristian Leme do Nascimento"
altura = 1.85
peso = 90
imc = peso / (altura * altura)

#"f-strings"
linha_1 = f"{nome} Tem {altura} de altura"
linha_2 = f"pesa {peso} quilos e seu IMC e"
linha_3 = f"{imc:.2f}"

print(linha_1)
print(linha_2)
print(linha_3)
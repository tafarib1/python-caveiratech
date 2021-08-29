numero = input('coloque o numero de pessoas da festa:')
pessoas = 0
lista = []

while pessoas <= int(numero):
    pessoa = input('coloque o nome de quem vai: ')
    pessoas += 1
    lista.append(pessoa)

for i in lista: print(i)
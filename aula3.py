print("voce é apto para o exercito?")

peso = input("qual seu peso ?")

altura = input('qual sua altura ?')

idade = input('qual sua idade ?')

if int(peso) >= 60 and float(altura) >= 1.70 and int(idade) >= 18 and int(idade) <= 20:
    print('vc é apto')
else:
    print('vc n é apto')
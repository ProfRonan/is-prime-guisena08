num = int(input('Digite um número: '))
if num <= 0:
    print('Número Inválido.')
else:
    primo =  True 
    for i in range(2, num):
        if num % i == 0:
            primo =  False
    if primo:
        print('primo')
    else:
        print('não primo')    
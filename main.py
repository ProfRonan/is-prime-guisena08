def is_prime(num):
    if num <= 1:
        return False
        print('Número inválido.')
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
           return  False
    return True
        
Console_insert = int(input('Digite um número:'))
if Console_insert <= 0:
        print('Número inválido.')
elif is_prime(Console_insert):
        print('Primo')
else:        
    print('Não primo')    
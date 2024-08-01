# bucle while
'''want_greet = 'S'  # importante dar un valor inicial

while want_greet == 'S':
    print('Hola qué tal!')
    want_greet = input('¿Quiere otro saludo? [S/N] ')
print('Que tenga un buen día')'''

#romper un bucle while

'''MAX_GREETS = 4

num_greets = 0
want_greet = 'S'

while want_greet == 'S':
    print('Hola qué tal!')
    num_greets += 1
    if num_greets == MAX_GREETS:
        print('Máximo número de saludos alcanzado')
        break
    want_greet = input('¿Quiere otro saludo? [S/N] ')
print('Que tenga un buen día')'''

#Comprobar la rotura
'''MAX_GREETS = 4

num_greets = 0
want_greet = 'S'

while want_greet == 'S':
    print('Hola qué tal!')
    num_greets += 1
    if num_greets == MAX_GREETS:
        print('Máximo número de saludos alcanzado')
        break
    want_greet = input('¿Quiere otro saludo? [S/N] ')
else:
    print('Usted no quiere más saludos')
print('Que tenga un buen día')'''


#Sentencia for

'''word = 'Python'

for letter in word:
    print(letter)'''

#Romper bucle for

'''word = 'Python'

for letter in word:
    if letter == 't':
        break
    print(letter)'''

#Secuencia de números

'''for i in range(0, 3):
    print(i)

for i in range(3):  # No hace falta indicar el inicio si es 0
    print(i)'''

#Usando el guión bajo
'''for _ in range(10):
    print('Repeat me 10 times!')'''

#Bucles anidados
'''for num_table in range(1, 10):
    for mul_factor in range(1, 10):
        result = num_table * mul_factor
        print(f'{num_table} * {mul_factor} = {result}')'''
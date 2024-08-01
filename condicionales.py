#Condicionales simples
'''temperature = 40

if temperature > 35:
    print('Aviso por alta temperatura')
else:
    print('Parámetros normales')'''

#Condicionales anidadas
'''temperature = 40

if temperature < 20:
    if temperature < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
else:
    if temperature < 30:
        print('Nivel naranja')
    else:
        print('Nivel rojo')'''

#Condicionales anidadas - elif

'''temperature = 28

if temperature < 20:
    if temperature < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
elif temperature < 30:
    print('Nivel naranja')
else:
    print('Nivel rojo')'''

#Asignaciones condicionales

'''temperature = 35

if temperature < 30:
    fire_risk = 'LOW'
else:
    fire_risk = 'HIGH'

print(fire_risk)'''

#Asignaciones condicionales - forma abreviada

'''temperature = 35

fire_risk = 'LOW' if temperature < 30 else 'HIGH'

print(fire_risk)'''

#Operadores de comparación

'''value = 8

value == 8

value != 8

value < 12

value <= 7

value > 4

value >= 9

4 <= x <= 12'''

#Operadores lógicos

'''and or not'''

'''x = 8

x > 4 or x > 12  # True or False

x < 4 or x > 12  # False or False

x > 4 and x > 12  # True and False

x > 4 and x < 12  # True and True

not(x != 8)  # not False'''

#Ejemplo

'''power = 10
signal_4g = 60

power > 25 and signal_4g > 10'''

'''power = 50
signal_4g = 20

power > 40 or signal_4g > 30'''

#Booleanos en condiciones 

'''is_cold = True

if is_cold == True:
    print('Coge chaqueta')
else:
    print('Usa camiseta')'''

'''if is_cold:
    print('Coge chaqueta')
else:
    print('Usa camiseta')'''

'''is_cold = False

if not is_cold:  # Equivalente a if is_cold == False
    print('Usa camiseta')
else:
    print('Coge chaqueta')'''

#Valor nulo
'''value = None

if value is None:
    print('Value is clearly None')
else:
    # value podría contener True, False (u otro)
    print('Value has some useful value')'''

'''value = 99

if value is not None:
    print(f'{value=}')'''

'''value = None

value is None

value == None'''

#Sentencia match-case
'''color = '#FF0000'

match color:
    case '#FF0000':
        print('🔴')
    case '#00FF00':
        print('🟢')
    case '#0000FF':
        print('🔵')
        
        
        color = '#AF549B'

match color:
    case '#FF0000':
        print('🔴')
    case '#00FF00':
        print('🟢')
    case '#0000FF':
        print('🔵')
    case _:
        print('Unknown color!')'''

#Patrones avanzados

'''point = (2, 5)

match point:
    case (x, y):
        print(f'({x},{y}) is in plane')
    case (x, y, z):
        print(f'({x},{y},{z}) is in space')

point = (3, 1, 7)

match point:
    case (x, y):
        print(f'({x},{y}) is in plane')
    case (x, y, z):
        print(f'({x},{y},{z}) is in space')'''

'''point = ('2', '5')

match point:
    case (x, y):
        print(f'({x},{y}) is in plane')
    case (x, y, z):
        print(f'({x},{y},{z}) is in space')'''

'''point = ('2', '5')

match point:
    case (int(), int()):
        print(f'{point} is in plane')
    case (int(), int(), int()):
        print(f'{point} is in space')
    case _:
        print('Unknown!')

point = (3, 9, 1)

match point:
    case (int(), int()):
        print(f'{point} is in plane')
    case (int(), int(), int()):
        print(f'{point} is in space')
    case _:
        print('Unknown!')'''

'''point = (8, 3, 5)

match point:
    case (int(x), int(y)):
        dist_to_origin = (x ** 2 + y ** 2) ** (1 / 2)
    case (int(x), int(y), int(z)):
        dist_to_origin = (x ** 2 + y ** 2 + z ** 2) ** (1 / 2)
    case _:
        print('Unknown!')

dist_to_origin'''

'''point = ('8', 3, 5)  # Nótese el 8 como "string"

match point:
    case (int(x), int(y)):
        dist_to_origin = (x ** 2 + y ** 2) ** (1 / 2)
    case (int(x), int(y), int(z)):
        dist_to_origin = (x ** 2 + y ** 2 + z ** 2) ** (1 / 2)
    case _:
        print('Unknown!')'''

'''# Lista de diccionarios
auths = [
    {'username': 'sdelquin', 'password': '1234'},
    {'email': 'sdelquin@gmail.com', 'token': '4321'},
    {'email': 'test@test.com', 'password': 'ABCD'},
    {'username': 'sdelquin', 'password': 1234}
]

for auth in auths:
    print(auth)
    match auth:
        case {'username': str(username), 'password': str(password)}:
            print('Authenticating with username and password')
            print(f'{username}: {password}')
        case {'email': str(email), 'token': str(token)}:
            print('Authenticating with email and token')
            print(f'{email}: {token}')
        case _:
            print('Authenticating method not valid!')
    print('---')'''


#Operador morsa

#Version tradicional
'''radius = 4.25
perimeter = 2 * 3.14 * radius
if perimeter < 100:
    print('Increase radius to reach minimum perimeter')
    print('Actual perimeter: ', perimeter)'''

#Versión con operador morsa

'''radius = 4.25
if (perimeter := 2 * 3.14 * radius) < 100:
    print('Increase radius to reach minimum perimeter')
    print('Actual perimeter: ', perimeter)'''


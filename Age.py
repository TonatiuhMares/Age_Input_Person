# Importación de Librerías
from datetime import datetime

# Fecha Actual
now = datetime.now()
añoact = now.year
mesact = now.month
diaact = now.day
print('Fecha actual: ',diaact, mesact, añoact)

# Datos de la persona
Persona1 = str(input('Ingresa tu nombre \n'))
dia1 = int(input('Ingresa tu día de nacimiento \n '))
mes1 = int(input('Ingresa tu mes de nacimiento (1-12) \n'))
año1 = int(input('Ingresa tu año de nacimiento \n'))


difaño = añoact-año1 
if mesact > mes1:
    print(f'Tienes {difaño} \n y tu cumpleaños acaba de pasar.')
elif mesact < mes1:
    print('Tienes: ',difaño - 1 ,' años')
    print('Por lo tanto este año cumplirás: ',difaño)
else:
    if diaact == dia1:
        print('Hoy es tu cumpleaños! Felicidades!! ')
    elif diaact > dia1:
        print(f'Acaba de pasar tu cumpleaños. Tienes {difaño} años.')
    elif diaact < dia1:
        print(f'Tu cumpleaños está muy cerca. Faltan: {dia1-diaact} día(s).')
        
        

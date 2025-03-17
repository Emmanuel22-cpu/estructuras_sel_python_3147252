'''
if es cascada:
Estructura de control que permite 
evaluar varias condiciones en 
cascada, es decir, si la primera 
condición no se cumple, 
se evalúa la siguiente
y así sucesivamente.
'''
# Ejemplo 1:
# Modificar el programa de votacion 
# para que considere la edad de 17
# años

edad = int(input("Ingresa tu edad: "))
if edad > 18:
    print("Puedes votar")
elif edad == 18:
    print("Puedes votar con contraseña")
elif edad == 17:
    print("Puedes votar el proximo año")
elif edad <= 10:
    print("Tienes registro civil")
elif edad < 17:
    print("No puedes votar aun")
print("Fin del programa")
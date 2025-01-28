#1

invitados = []

print("Bienvenido al programa")
continuar = 'si'
while continuar == 'si':
    nombre = input("Ingrese el nombre del invitado: ")
    invitados.append(nombre)
    print(f"{nombre} ha sido invitado.")
    continuar = input("¿Desea invitadar a alguien más?: ")
print("Lista de invitados:")
for invitado in invitados:
    print(invitado)
    
#2

def numero_rango():
    while True:
            numero = int(input("Dame un número entre 5 y 10: "))
            if 5 <= numero <= 10:
                return numero
            else:
                print("El número no está en el rango. Dame un numero entre 5 y 10.")
numero_en_rango = numero_rango()
print(f"El número {numero_en_rango} está en el rango.")

#Las dos principales diferencias entre el ciclo For y el ciclo While son que en el ciclo for el creador tiene una idea de cuántas iteraciones se realizará, en cambio, en el ciclo whuile no ya que el cilco se correrá n veces se cumpla la condición. Además, el ciclo for iterará en función de listas, tuplas, etc (secuencias), y el ciclo while operará mediante una función.

#3

def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicación(a, b):
    return a * b
def división(a, b):
    return a / b
num = 10
num2 = 5

print(f"Suma: {num} + {num2} = {suma(num, num2)}")
print(f"Resta: {num} - {num2} = {resta(num, num2)}")
print(f"Multiplicación: {num} * {num2} = {multiplicación(num, num2)}")
print(f"División: {num} / {num2} = {división(num, num2)}")

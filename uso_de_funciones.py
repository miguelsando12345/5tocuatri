""" uso de funciones en py 
funcion que salude 
funcion que recibe 2 argumentos y hace una operacion matematica """

nombre = "Miguel"
print("Hola, mi niombre es: " , nombre )

#funcion que recibe 2 argumentos y hace una operacion matematica 
def multiplicacion (a, b):
  
    return a * b


resultado = multiplicacion(5, 3)
print("El resultado es: " , resultado)

#Ejercicio 3 -- pedir al usuario 2 numeros y pasarlos como argumentos y realizar una suma 


# Pedimos al usuario dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

resultado = numero1 + numero2 
print ("el resultado de la suma es:" , resultado)



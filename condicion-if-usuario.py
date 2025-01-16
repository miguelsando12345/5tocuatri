#En este ejercicio vamos a validar un usuario y contraseña d eusuario 
#si el usuario es correcto y la contraseña es corrccta
#entonces se imprime un mensaje de vienvenida 

#se pide el usuario que ingrese su usuario 
usuario = input ("Ingrese un usuario: ")
#Se pide al usuario que ingrese su contraseña 
contraseña = input ("ingrese su contraseña:")
# se valida si el usuario es igual a "admi" y la contraseña es igual a "admin123"
if usuario == "admin" and contraseña == "admin123":
    print("Bienvenido a el sistema")
else:
    print("Usuario o contraseña incorrecta")

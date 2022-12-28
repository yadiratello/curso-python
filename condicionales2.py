print("Verificacion de acceso")

edadUsuario = int(input("Introduce tu edad:"))


if edadUsuario < 18:
    print("No tienes acceso")
elif edadUsuario>150:
    print("Edad incorrecta")
else: 
    print("Puedes pasar")

#Crea un programa que pida dos números por teclado. El programa tendrá una función llamada “DevuelveMax” encargada de devolver el número más alto de los dos introducidos.
"""
print("Programa que devuelve el maximo de 2 numeros")

num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))

def devuelveMax(num1,num2):
    if(num1 > num2):
        return num1
    else:
        return num2

#llamar a la funcion
print(devuelveMax(num1,num2))    
"""


#Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por teclado).

nombre = input("Ingrese nombre: ")
direccion = input("Ingrese direccion: ")
telefono = input("Ingrese telefono: ")

datosPersonales = [nombre, direccion, telefono]

print("Los datos personales son: Nombre: " + datosPersonales[0] + " Direccion: " + datosPersonales[1] + " Telefono: "+datosPersonales[2])

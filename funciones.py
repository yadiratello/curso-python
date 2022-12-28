#funciones predefinidas(propias del lenguaje) como print() :


#creando una funcion sin parametros
def mensaje():
    print("Estamos aprendiendo python")


#llamando a la funcion
mensaje()
print("Hola mundo!")
mensaje()



#funcion suma que tendra argumentos
def suma(num1=1 ,num2=2):
    resultado = num1 + num2
    return resultado
    

print(suma(14,14))
print(suma())
print(suma(2,3))
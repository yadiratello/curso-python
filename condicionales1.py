print("Programa de evaluacion de notas de alumno")

#input(): recibe un valor por teclado
#int(): castea a int
notaAlumno = int(input("Introduce la nota del alumno:"))

#creando funcion
def evaluacionAlumno(nota):
    valoracion = "aprobado"
    #evaluar la nota
    if nota<11:
        valoracion = "desaprobado"
    #fin del if
    return valoracion


#llamar a la funcion
print(evaluacionAlumno(notaAlumno))



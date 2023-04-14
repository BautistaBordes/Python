

#10. Dada una lista de nombres de estudiantes y dos listas con sus notas en un curso, escriba un
#programa que manipule dichas estructuras de datos para poder resolver los siguientes puntos:
#A. Generar una estructura con todas las notas relacionando el nombre del estudiante con las
#notas. Utilizar esta estructura para la resolución de los siguientes items.
#B. Calcular el promedio de notas de cada estudiante.
#C. Calcular el promedio general del curso.
#D. Identificar al estudiante con la nota promedio más alta.
#E. Identificar al estudiante con la nota más baja.




nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]



def armarLista(nombres,notas1,notas2):
    """ Creo un diccionario que va tener como clave su nombre y el valor va a ser una tupla con sus dos notas asociadas"""
    nombres = nombres.replace('\n','').replace("'",'').replace(' ','').split(',')
    return dict(zip(nombres, zip(notas1, notas2)))

DicAlumnosConNotas=armarLista(nombres,notas_1,notas_2)

promedioNotas = lambda nota1,nota2:((nota1+nota2)/2)

alumnosNotas={'notaPromedioAlta':('',-1),'notaBaja':('',99999)}
def calcularNotaPromedioMasAlta(prom,alumno,alumnosNotas):
    """ Calcula la nota promedio mas alta """
    if prom > alumnosNotas['notaPromedioAlta'][1]:
        alumnosNotas['notaPromedioAlta'] = (alumno, prom)
        
def calcularNotaMasBaja(elem,alumnosNotas):
    """ Calcula la nota mas baja """
    for nota in elem[1:2]:
        if nota < alumnosNotas['notaBaja'][1]:
            alumnosNotas['notaBaja'] = (elem[0],nota)

promedioTotal= lambda notas,lista:(notas/len(lista) )
 

notasTotalAlumnos=0

for nombre, notas in DicAlumnosConNotas.items():
    promNotasAlumno = promedioNotas(notas[0], notas[1])
    print(f'El alumno {nombre} tiene un promedio de {promNotasAlumno}')
    notasTotalAlumnos += promNotasAlumno
    calcularNotaPromedioMasAlta(promNotasAlumno, nombre, alumnosNotas)
    calcularNotaMasBaja((nombre, notas[0], notas[1]), alumnosNotas)
    

print(f'El promedio general del curso es {promedioTotal(notasTotalAlumnos,DicAlumnosConNotas):.3f} ')
print(f'El alumno con la nota mas baja es {alumnosNotas["notaBaja"]}')
print(f'El alumno con nota promedio mas alta es {alumnosNotas["notaPromedioAlta"]}')

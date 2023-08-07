import sqlite3 as sql
from os import system
import sys

cnn = sql.connect('Escolar.db')

def createTable():
    cursor = cnn.cursor()
    cursor.execute(
        """Create Table Estudiantes(
            Rne integer,
            Nombre text,
            Curso text,
            Promedio float,
            Pago text
        )
    """)
    cnn.commit()
    cnn.close()

def ingresarDatosDeEstudiante():
    cursor = cnn.cursor()
    inp = input("Ingrese el rne del nuevo alumno: ")
    inp1 = input("ingrese el nombre del nuevo alumno: ")
    inp2 = input("ingrese el Curso del nuevo alumno: ")
    p1 = input("ingrese el Promedio del nuevo estudiante: ")
    Pago = input("El estudiante nuevo Pago: ")
    instruccion = f"insert into Estudiantes Values({inp}, '{inp1}', '{inp2}', {p1}, '{Pago}')"
    cursor.execute(instruccion)
    cnn.commit()
    system("cls")

def borrarTabla():
    cursor = cnn.cursor()
    instruccion = "drop table stramers"
    cursor.execute(instruccion)
    cnn.commit()
    cnn.close()

def comprobarEstudiante(Rne):
    cursor = cnn.cursor()
    instruccion = f"SELECT Count(Rne) FROM Estidiantes where Rne = '{Rne}'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    cnn.commit()
    cnn.close()

    for x in datos:
        separador = ", "  # Aqui puedes poner si prefieres ", "
        cadena = separador.join(str(parte) for parte in x)
        print(cadena)

def comprobarEstudiante(Rne):
    cursor = cnn.cursor()
    instruccion = f"SELECT Count(Rne) FROM Estudiantes where Rne = '{Rne}'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    datos1= datos[0]
    return datos1[0]

def verDatosdelEstudiante(Rne):
    cursor = cnn.cursor()
    instruccion = f"SELECT Rne, Nombre, Curso, Promedio, Upper(Pago) FROM Estudiantes where Rne = '{Rne}'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    datos1= datos[0]
    datos0 = datos1[0]
    datos2= datos1[1]
    datos3= datos1[2]
    datos4= datos1[3]
    datos5= datos1[4]
    return f"""
    ****************************
    *    Rne: {datos0}         *
    *    Nombre: {datos2}      *
    *    Curso: {datos3}       *
    *    Promedio: {datos4}    *
    *    Pago: {datos5}    *
    ****************************
    """
def estudiantePago(Rne):
    cursor = cnn.cursor()
    instruccion = f"SELECT Count(Rne) FROM Estudiantes where pago like 'si%' and Rne = '{Rne}'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    datos1= datos[0]
    return datos1[0]

def actualizarDato(Pago):
    cursor = cnn.cursor()
    instruccion = f"Update Estudiantes set Pago = 'si' where Rne = {Pago}"
    cursor.execute(instruccion)
    cnn.commit()
    return "datos actualizados exitosamente"

def actualizarTodo(Pago):
    cursor = cnn.cursor()
    instruccion = f"Update Estudiantes set Pago = 'no' where Pago = '{Pago}'"
    cursor.execute(instruccion)
    cnn.commit()
    return "datos actualizados exitosamente"



if __name__ =="__main__":
    pass
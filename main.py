from os import system
import database as base
print("***************************")
print("* Sebastian Alvarez #2    *")
print("***************************")
print("* Sistema Escolar *")
print("***************************\n\n")

def primerasPreguntas():
    print("***************************")
    print("* 1. Consultar Estudiante *")
    print("***************************")
    print("* 2. Crear Estudiante     *")
    print("***************************\n")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        system("cls")
        rne = input("ingrese el rne del estudiante: ")
        while base.comprobarEstudiante(rne) == 0:
            print("Parece que el estudiante no existe")
            rne = input("ingrese el rne del estudiante: ")
            system("cls")

        while base.estudiantePago(rne) == 0:
            print("Lo siento el estudiante no pago el anio")
            anio = input("Desea pagar el anio: ")
            system("cls")

            if anio == "si" or anio == "SI":
                print("****************")
                print("* Precio: 1200$*")
                print("****************")
                pago = float(input("Ingrese la cantidad del pago: "))
                if pago == 1200:
                    base.actualizarDato(rne)
        system("cls")
        print(base.verDatosdelEstudiante(rne))    
        salir = input("Desea salir? S/N: ")
        if salir == 'S' or salir == 's':
            pass
        else:
            return primerasPreguntas
        
                             
    elif opcion == "2":
        system("cls")
        base.ingresarDatosDeEstudiante()
        salir = input("Desea salir? S/N: ")
        if salir == 'S' or salir == 's':
            pass
        else:
            return primerasPreguntas()
    else:
        system("cls")
        return primerasPreguntas()




if __name__ == "__main__":
    primerasPreguntas()
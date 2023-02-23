from agregar import *
from actualizar import *
from eliminar import *
from leer import *
acumulador={}
#EJERCICIO DE BIBLIOTECA AGREGANDO FECHAS
while True:
    print("-"*50)
    print(
    """
    ----PROGRAMA QUE ALMACENA INFORMACION DE BIBLIOTECA----
    
    Seleccione una acción.
    1. registrar usuario.
    2. actualizar usuario.
    3. eliminar usuario.
    4. visualizar usuarios
    (x) salir
    """
    )
    seleccion = input("selección: ")

    if seleccion == "1":
        agregar_usuario(acumulador)
        

    if seleccion =="2":
        print(acumulador)
        actualizar_usuario(acumulador)
    
    if seleccion == "3":
        print(acumulador)
        eliminar_usuario(acumulador)
    
    if seleccion == "4":
        leer_usuario(acumulador)
    if seleccion == "x":
        print("HASTA PRONTO")
        break
    print("-"*50)

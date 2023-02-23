def agregar_usuario(
    dicc:dict
)-> dict:
    """REGISTRAR USUARIO

    Args:
        nombre = Nombre del usuario
        libro = nombre del libro
        ---FECHA INGRESADA POR EL USUARIO---
        dia = dia de la entrega
        mes = mes de la entrega
        año = año de la entrega

    Returns:
        
    """
    nombre=str(input("Ingrese su nombre: "))
    libro =str(input("Ingrese el nombre del libro: "))
 
    
    print(" ---INGRESE LA FECHA--- ")
    from datetime import date
    hoy=date.today()
    dia=input("ingrese dia: ".format(hoy.day))
    mes=input("ingrese mes: ".format(hoy.month))
    año=input("ingrese año: ".format(hoy.year))
    hoy=dia+'-'+mes+'-'+año
    dicc[nombre] = libro+' => '+hoy

        
            

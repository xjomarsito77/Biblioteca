def actualizar_usuario(
    dicc:dict
    
):
    """ACTUALIZAR DATO DEL DICCIONARIO

    Args:
        antius = usuario antiguo
        nombre = el nuevo nombre 
        libro = el nuevo libro

    Returns:
        
    """
    
    antius=input("ingrese nombre del usuario antiguo: ")
    nombre =input("Ingrese el nuevo nombre: ")
    libro =input("Ingrese el nombre del libro: ")
    
    
    print(" ---INGRESE LA FECHA--- ")
    from datetime import date
    today=date.today()
    dia=input("ingrese dia: ".format(today.day))
    mes=input("ingrese mes: ".format(today.month))
    año=input("ingrese año: ".format(today.year))
    fecha_n=dia+'-'+mes+'-'+año
    dicc.pop(antius)
    dicc[nombre] = libro+' => '+fecha_n
    
    
    

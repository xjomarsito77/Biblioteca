def eliminar_usuario(
    diccionario:dict
)-> dict:
    """ELIMINAR USUARIO

    Args:
        nombre = nombre del usuario que va a eliminar

    Returns:
        dict: _description_
    """
    nombre=input("ingrese nombre del usuario a eliminar: ")
    diccionario.pop(nombre)
    
         
        
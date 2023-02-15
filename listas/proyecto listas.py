# -*- coding: utf-8 -*-
"""
Apellidos y Nombres: Pareja Ramos Abel 
"""
def agregar_usuario():
    global usuarios
    id = int(input("ingrese el ID: "))
    nombre = input("ingrese el nombre: ")
    direc = input("ingrese su direccion: ")
    cel = int(input("ingrese su numero de celular: "))
    
    usuarios[id] = nombre,direc,cel
    print(usuarios)
    
    
def eliminar_usuario(id):
    global usuarios
    del(usuarios[id])
    print("Eliminado")
    
    
def listar():
    global usuarios
    for user in usuarios: 
        print(
    """
        ID: {}
        Nombre: {}
        Direccion: {}
        Celular: {}
              
              
    """.format(user,usuarios[user][0],usuarios[user][1],usuarios[user][2]))

usuarios = {}
while True:
    print("..aplicaciones en python..")
    print("[1]..agregar usuario..")
    print("[2]..eliminar usuario..")
    print("[3]..listar usuario..")
    print("[4]..salir..")
    try:
        opcion = int(input("\nSeleccione una opcion: "))
        
        if opcion ==1:
            agregar_usuario()
        elif opcion == 2:
            id =int(input("ingrese el id del usuario"))
            eliminar_usuario(id)
        elif opcion == 3:
            listar()
        elif opcion == 4:
            break

    except:
        print("por favor ingrese los valores correctos:  ")


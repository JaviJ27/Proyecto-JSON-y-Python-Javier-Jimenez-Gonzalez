from Funciones import listar_marca_modelo, contar_marca, mostrar_info_componente, buscar_especificacion, modificar_componente
comprobador = True
while comprobador == True:
    print("-----------------")
    print("| Proyecto JSON |")
    print("-----------------")
    print("\n1. Listar marca y modelo")
    print("2. Contar veces que aparece una marca")
    print("3. Mostrar toda la información de un componente de un PC")
    print("4. Mostrar qué PCs tienen una especificación concreta")
    print("5. Modificar la información sobre el componente de un PC")
    print("6. Salir")
    opcion = input("\nSelecciona una opción (1-6): ")
    
    if opcion == "1":
        listar_marca_modelo()
    elif opcion == "2":
        contar_marca()
    elif opcion == "3":
        mostrar_info_componente()
    elif opcion == "4":
        buscar_especificacion()
    elif opcion == "5":
        modificar_componente()
    elif opcion == "6":
        print("¡Saliendo del programa!")
        comprobador = False

    else:
        print("Opción no válida. Por favor, selecciona un número del 1 al 6.")
    print("\n" + "="*50)

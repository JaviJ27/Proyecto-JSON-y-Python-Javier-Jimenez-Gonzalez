import json

with open('pcs.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

def listar_marca_modelo():
    col_componente = 20
    col_fabricante = 15
    col_modelo = 35
    for pc_name, pc_data in data.items():
        print(f"\n=== Componentes de {pc_name} ===")
        print(f"{'Componente'.ljust(col_componente)} {'Fabricante'.ljust(col_fabricante)} {'Modelo'.ljust(col_modelo)}")
        for component_name, component_data in pc_data.items():
            fabricante = component_data.get("Fabricante", "No especificado")
            modelo = component_data.get("Modelo", "No especificado")
            print(f"{component_name.ljust(col_componente)} {fabricante.ljust(col_fabricante)} {modelo.ljust(col_modelo)}")
    input("\n\nPuse cualquier tecla para continuar")
            
def contar_marca():
    fabricante_buscar = input("Introduce el nombre del fabricante a buscar: ")
    contador = 0
    for pc_name, pc_data in data.items():
        for component_name, component_data in pc_data.items():
            fabricante = component_data.get("Fabricante", "No especificado")
            if fabricante.lower() == fabricante_buscar.lower():
                contador += 1
    if contador > 0:
        print(f"El fabricante '{fabricante_buscar}' aparece {contador} veces en el JSON.")
    else:
        print(f"El fabricante '{fabricante_buscar}' no aparece en el JSON.")
    input("\n\nPuse cualquier tecla para continuar")

def mostrar_info_componente():
    pc_buscar = input("Introduce el nombre del PC (PC1, PC2 o PC3): ")
    componente_buscar = input("Introduce el componente (ej. CPU, MemoriaRAM, etc.): ")
    if pc_buscar not in data:
        print(f"El PC '{pc_buscar}' no se encuentra en el JSON.")
    else:
        pc_data = data[pc_buscar]
        if componente_buscar not in pc_data:
            print(f"El componente '{componente_buscar}' no está en el PC '{pc_buscar}'.")
        else:
            componente_data = pc_data[componente_buscar]
            col_especificacion = 25
            col_valor = 40
            print(f"\n=== Información de {componente_buscar} en {pc_buscar} ===")
            print(f"{'Especificación'.ljust(col_especificacion)} {'Valor'.ljust(col_valor)}")
            def mostrar_datos(datos, prefijo=""):
                for key, value in datos.items():
                    if isinstance(value, dict):
                        mostrar_datos(value, prefijo=f"{prefijo}{key}.")
                    else:
                        especificacion = f"{prefijo}{key}"
                        print(f"{especificacion.ljust(col_especificacion)} {str(value).ljust(col_valor)}")
            mostrar_datos(componente_data)
    input("\n\nPuse cualquier tecla para continuar")

def buscar_especificacion():
    componente = input("Introduce el componente (ej. MemoriaRAM, CPU, etc.): ")
    especificacion = input("Introduce la especificación (ej. Capacidad, Modelo, etc.): ")
    valor = input("Introduce el valor (ej. 32GB, Ryzen 7 9800X3D, etc.): ")
    pcs_coincidentes = []
    for pc_name, pc_data in data.items():
        if componente in pc_data:
            componente_data = pc_data[componente]
            if especificacion in componente_data and str(componente_data[especificacion]).lower() == valor.lower():
                pcs_coincidentes.append(pc_name)
            elif isinstance(componente_data.get(especificacion), dict):
                sub_dict = componente_data[especificacion]
                coincide = any(str(sub_value).lower() == valor.lower() for sub_key, sub_value in sub_dict.items())
                if coincide:
                    pcs_coincidentes.append(pc_name)
    if pcs_coincidentes:
        print(f"\nPCs que tienen {componente} con {especificacion} = {valor}:")
        for pc in pcs_coincidentes:
            print(f"- {pc}")
    else:
        print(f"\nNo se encontraron PCs con {componente} que tengan {especificacion} = {valor}.")
    input("\n\nPuse cualquier tecla para continuar")

def modificar_componente():
    pc_buscar = input("Introduce el nombre del PC (PC1, PC2 o PC3): ")
    componente_buscar = input("Introduce el componente (ej. CPU, MemoriaRAM, etc.): ")
    especificacion_buscar = input("Introduce la especificación a modificar (ej. Modelo, Caché.L1, Frecuencia.Boost): ")
    nuevo_valor = input("Introduce el nuevo valor: ")
    if pc_buscar not in data:
        print(f"El PC '{pc_buscar}' no se encuentra en el JSON.")
    else:
        pc_data = data[pc_buscar]
        if componente_buscar not in pc_data:
            print(f"El componente '{componente_buscar}' no está en el PC '{pc_buscar}'.")
        else:
            componente_data = pc_data[componente_buscar]
            def modificar_datos(datos, espec_path, valor):
                partes = espec_path.split('.')
                current = datos
                for i, parte in enumerate(partes):
                    if i == len(partes) - 1:
                        if parte in current:
                            current[parte] = valor
                            return True
                        return False
                    else:
                        if parte in current and isinstance(current[parte], dict):
                            current = current[parte]
                        else:
                            return False
                return False
            if modificar_datos(componente_data, especificacion_buscar, nuevo_valor):
                with open('pcs.json', 'w', encoding='utf-8') as file:
                    json.dump(data, file, indent=2, ensure_ascii=False)
                print(f"Se ha modificado '{especificacion_buscar}' de {componente_buscar} en {pc_buscar} a '{nuevo_valor}'.")
            else:
                print(f"La especificación '{especificacion_buscar}' no se encontró en {componente_buscar} de {pc_buscar}.")
    input("\n\nPuse cualquier tecla para continuar")

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
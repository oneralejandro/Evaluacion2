lista = [];
total_compras = 0;
while True:
    print("Menú:")
    print("1. Agregar Compra ")
    print("2. Mostrar Compras ")
    print("3. Mostrar total gastado ")
    print("4. Salir")


    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Seleccionaste la Opción 1")
        agregarCompras = int(input("ingrese valor de la compra"))
        lista.append(agregarCompras)
        print("Compra Agregada exitosamente !")

    elif opcion == "2":
        print("Seleccionaste la Opción 2")
        print("Compras : ")
        for i, listas in enumerate(lista,1):
            print(i,".$",listas)







    elif opcion == "3":
        print("Seleccionaste la Opción 3")
        print("El monto total de lacompra es ",sum(lista))

    elif opcion == "4":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
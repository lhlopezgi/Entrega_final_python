#Proyecto 1 calculadora

#Definir funciones


"""
def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

#para la funcion division se incluye el descarte de division entre cero
def division(a,b):
    if b != 0:
        return a/b
    else:
        return "Error: Division en cero"


#Se realiza la funcion que mostrara el menu en pantalla
def mostrar_menu():
    print("Calculadora Basica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")


#se crea un ciclo para que el programa se ejecute hasta que se elija la opcion 5

while True:
    mostrar_menu()
    opcion = input("Elige una opcion: ")
    if opcion == "5":
        print("salir del programa")
        break

    if opcion in ["1", "2", "3", "4"]:
        num1 = float(input("ingrese el primer numero:"))
        num2 = float(input("ingrese el segundo numero:"))

        if opcion == "1":
            print(f'Resultado: {suma(num1, num2)}')
        elif opcion == "2":
            print(f'Resultado: {resta(num1, num2)}')
        elif opcion == "3":
            print(f'Resultado: {multiplicacion(num1, num2)}')
        elif opcion == "4":
            print(f'Resultado: {division(num1, num2)}')
    else:
        print("Opcion no valida, por favor intentar de nuevo")
"""

"""

#Proyecto 2 gestion de contactos

class Contacto: #definimos la clase y el nombre de la clase
    def __init__ (self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

def mostrar_menu():
    print("Gestion de contacto")
    print("1. Agregar contacto")
    print("2. Mostrar contacto")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

contactos = []

while True:
    mostrar_menu()
    opcion = input("Elije una opcion: ")
    if opcion == "5":
        print("saliendo del programa.")
        break

    if opcion == "1":
        nombre = input("Ingresa el nombre: ")
        telefono = input("Ingresa el telefono: ")
        contacto = Contacto(nombre, telefono)
        contactos.append(contacto) #se utiliza para agregar un elemento al final de la lista
        print("contacto agregado. ")
    elif opcion == "2":
         for c in contactos:
            print(f'Nombre: {c.nombre},Telefono: {c.telefono}' )
    elif opcion == "3":
        nombre = input(" Ingresa el nombre a buscar. ")
        encontrado = False
        for c in contactos:
            if c.nombre == nombre:
                print(f'Nombre: {c.nombre},Telefono: {c.telefono}' )
                encontrado = True
                break
            if not encontrado:
                print("Contacto no encontrado")
    elif opcion == "4":
        nombre = input("Ingresa el nombre a eliminar: ")
        for c in contactos:
            if c.nombre == nombre:
                contactos.remove(c)
                print("contacto eliminado.")
                break
    else:
        print("opcion no valida . Seguir intentando")

"""

"""
#Proyecto 3 Gestion de inventario

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self):
        try:
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(nombre, cantidad, precio)
            self.productos.append(producto)
            print("Producto agregado exitosamente.")
        except ValueError:
            print("Error: Ingrese datos válidos.")

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos:
                print(producto)

    def buscar_producto(self):
        nombre = input("Ingrese el nombre del producto a buscar: ")
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                print(producto)
                return
        print("Producto no encontrado.")

    def actualizar_cantidad(self):
        nombre = input("Ingrese el nombre del producto a actualizar: ")
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                try:
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                    producto.cantidad = nueva_cantidad
                    print("Cantidad actualizada exitosamente.")
                    return
                except ValueError:
                    print("Error: Ingrese una cantidad válida.")
                    return
        print("Producto no encontrado.")

    def eliminar_producto(self):
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                self.productos.remove(producto)
                print("Producto eliminado exitosamente.")
                return
        print("Producto no encontrado.")


def main():
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Inventario ---")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Actualizar cantidad")
        print("5. Eliminar producto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            inventario.agregar_producto()
        elif opcion == "2":
            inventario.mostrar_productos()
        elif opcion == "3":
            inventario.buscar_producto()
        elif opcion == "4":
            inventario.actualizar_cantidad()
        elif opcion == "5":
            inventario.eliminar_producto()
        elif opcion == "6":
            print("Gracias por usar el sistema de inventario. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()

"""

"""
#Proyecto 4 sistema de gestion de tareas

class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = "pendiente"

    def __str__(self):
        return f"Título: {self.titulo}\nDescripción: {self.descripcion}\nEstado: {self.estado}"


class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self):
        titulo = input("Ingrese el título de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        tarea = Tarea(titulo, descripcion)
        self.tareas.append(tarea)
        print("Tarea agregada exitosamente.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
        else:
            for i, tarea in enumerate(self.tareas, 1):
                print(f"\nTarea {i}:\n{tarea}")

    def buscar_tarea(self):
        titulo = input("Ingrese el título de la tarea a buscar: ")
        for tarea in self.tareas:
            if tarea.titulo.lower() == titulo.lower():
                print(tarea)
                return
        print("Tarea no encontrada.")

    def actualizar_estado(self):
        titulo = input("Ingrese el título de la tarea a actualizar: ")
        for tarea in self.tareas:
            if tarea.titulo.lower() == titulo.lower():
                tarea.estado = "completada"
                print("Estado de la tarea actualizado a 'completada'.")
                return
        print("Tarea no encontrada.")

    def eliminar_tarea(self):
        titulo = input("Ingrese el título de la tarea a eliminar: ")
        for tarea in self.tareas:
            if tarea.titulo.lower() == titulo.lower():
                self.tareas.remove(tarea)
                print("Tarea eliminada exitosamente.")
                return
        print("Tarea no encontrada.")


def main():
    gestor = GestorTareas()

    while True:
        print("\n--- Sistema de Gestión de Tareas ---")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Buscar tarea")
        print("4. Actualizar estado de tarea")
        print("5. Eliminar tarea")
        print("6. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                gestor.agregar_tarea()
            elif opcion == 2:
                gestor.mostrar_tareas()
            elif opcion == 3:
                gestor.buscar_tarea()
            elif opcion == 4:
                gestor.actualizar_estado()
            elif opcion == 5:
                gestor.eliminar_tarea()
            elif opcion == 6:
                print("Gracias por usar el sistema de gestión de tareas. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")


if __name__ == "__main__":
    main()

"""
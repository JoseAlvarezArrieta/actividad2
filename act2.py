import os


class Empleado(): 
    listE = []   # hacemos un vector.
    def __init__(self):
        self.emp = {} # Hacemos un diccionario           
    

    def añadirEmp(self):   # funcion para agregar empleados
        print ("===> Añadiendo Empleado <====")
        self.emp = {
            "nombre": input("Digite el Nombre del empleado: => "),
            "edad": input("Digite la edad del empleado: => "),
            "Cargo": input("Digite el cargo del empleado: => "),    
            "Salario": input("Digite el salario del empleado: => ") }     

        # llamamos al vector para incluya la  lista por medio de append  
        self.listE.append(self.emp) 



    # funcion para mostar los empleados
        
    def mostrarEmp(self):
        print ("===> Mostrando Empleados <====")
        print(self.listE) 
       # Mostramos la lista de empleados

    # funcion para eliminar empleados
    def eliminarEmp(self):
        print ("===> Eliminando Empleado <====")
        elim = str(input("Digite el nombre del empleados a eliminar: "))
def main():

    cons = "s"

    while cons == "s": # mostrando el menu
        print("*************************** ")
        print("+  Bienvenido al menu + ")
        print("Escoja una opción: ")
        print("1. Añadir Persona =")
        print("2. Eliminar Persona =")
        print("3. Mostrar Persona =")
        print("4. Añadir Empleado =")
        print("5. Eliminar Empleado =")
        print("6. Mostrar Empleado =")
        print("0. salir  =>")
        print("*************************** ")

        opc = int(input("Digite la opción: ")) # Digitando la opcion del menu
        
        print()
        if opc==1:
            os.system ("clear")
            persona = Persona() # llamando la clase persona
            persona.añadirPe()
        elif opc==2:
            os.system ("clear")            
            persona.eliminarPe() # llamando la funtion eliminar  persona      
        elif opc==3:
            os.system ("clear")            
            persona.mostrarPe() # llamando la funtion listar persona
        elif opc==4:
            os.system ("clear")
            empleado = Empleado() # llamando la clase empleado
            empleado.añadirEmp()
        elif opc==5:
            os.system ("clear")            
            empleado.eliminarEmp() # llamando la funtion eliminar empleado       
        elif opc==6:
            os.system ("clear")            
            empleado.mostrarEmp() # llamando la funtion listar empleado
        elif opc==0:
            os.system ("clear")
            print(" See you later. Bye ")    
        cons = input(" Desea continuar s/n:.. ")
        os.system ("clear")


if __name__ == "__main__":
    main()

import os

# Hacemos la clase Persona
class Persona(): 
    listP = []   # hacemos un vector.
    def __init__(self):
        self.person = {} # Hacemos un diccionario           
    

    def añadirPe(self):   # funcion para agregar Personas
        print ("===> Añadiendo Persona <====")
        self.person = {
            "nombre": input("Digite el Nombre: => "),
            "edad": input("Digite la edad: => "),
            "hobbie": input("Digite su hobbie: => ") }     

        # llamamos al vector para incluya la  lista por medio de append  
        self.listP.append(self.person) 



    # funcion para mostar los Personas
    
    def mostrarPe(self):
        print ("===> Mostrando Personas <====")
        print(self.listP) 
       # Mostramos la lista de Personas

    # funcion para eliminar Personas
    def eliminarPe(self):
        print ("===> Eliminando Persona <====")
        elim = str(input("Digite el nombre de la Persona a eliminar: "))

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

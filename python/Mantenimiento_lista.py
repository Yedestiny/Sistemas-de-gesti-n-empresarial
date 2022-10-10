# Angel Javier Bailon Gracia
class Articulo():
    def __init__(self,codigo,nombre,precio,descripcion):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

class Lista():
    cesta = []

    def agregar_cesta(self,nuevo_articulo):
        self.cesta.append({"codigo":nuevo_articulo.codigo,"nombre":nuevo_articulo.nombre,"precio":nuevo_articulo.precio,"descripcion":nuevo_articulo.descripcion})


    def listar(self):
        if len(self.cesta)!=0:
            print("--------------MI CESTA------------------")
            for i in range(0, len(self.cesta)):
                print("ARTICULO: ",self.cesta[i]["nombre"])
                print("Codigo del articulo: " , self.cesta[i]["codigo"])
                print("nombre del articulo: " , self.cesta[i]["nombre"])
                print("precio del articulo: " , self.cesta[i]["precio"])
                print("descripcion del articulo: " , self.cesta[i]["descripcion"],"\n")
        else:
            print("La cesta esta vacia")

    def borrar(self):
        try:
            self.id_producto_a_borrar= int(input("Id del producto que quieres borrar: "))

            self.encontrado = False
            for i in range(0, len(self.cesta)):

                if self.cesta[i]["codigo"] == self.id_producto_a_borrar:
                    print(self.cesta)
                    self.cesta.pop(i)
                    print("Articulo borrado \n")
                    self.encontrado = True

            if self.encontrado==False:
                print("ID NO ENCONTRADO")

        except:
            print("LOS ID SOLO SE IDENTIFICAN CON NUMEROS")

    def buscar(self,busqueda):
        self.busqueda = busqueda
        self.resultado =[]
        for i in self.cesta:
            if self.busqueda in i["nombre"] :
                self.resultado.append(i)

        print("--------RESULTADO DE BUSQUEDA------------")
        for i in range(0, len(self.resultado)):
            print("ARTICULO: ", self.resultado[i]["nombre"])
            print("Codigo del articulo: ", self.resultado[i]["codigo"])
            print("nombre del articulo: ", self.resultado[i]["nombre"])
            print("precio del articulo: ", self.resultado[i]["precio"])
            print("descripcion del articulo: ", self.resultado[i]["descripcion"], "\n")





articulo1 =  Articulo(21,"Destornillador",54,"Destornillador de estrella")
articulo2 =  Articulo(2211,"Holo",54,"Destornillador de estrella")

milista = Lista()

milista.agregar_cesta(articulo1)
milista.agregar_cesta(articulo2)

acabar=True
while acabar:
    accion = input("Quieres listar, agregar, borrar , buscar o salir?: ")
    if accion=="listar":
        milista.listar()
    elif accion=="agregar":
        nuevo_articulo= Articulo(int(input("Id del producto: ")),input("Nombre del producto: "),int(input("Precio: ")),input("Descripcion: "))
        milista.agregar_cesta(nuevo_articulo)
    elif accion=="borrar":
        milista.borrar()
    elif accion=="buscar":
        milista.buscar(input("Que quieres buscar: "))
    elif accion=="salir":
        acabar=False
        milista.listar()
        print("------ FIN DEL PROGRAMA--------")
    else:
        print("Comando desconocido, prueba otra vez")






import re
import json

#####################################################################################################################################
##CLASE CLIENTE: atributos y metodos del objeto cliente 

class Cliente: 

    def __init__(self, nombreCompleto, gmail, contrasena, id):
        self.id = id
        self.nombreCompleto = nombreCompleto
        self.gmail = gmail
        self.contrasena = contrasena
        self.tarjeta = Tarjeta('', 0, 0, 0, 0)
        self.carrito = Carrito()

    def __str__(self):
        return (f"\n||  Nombre Completo: {self.nombreCompleto}  \n||  Gmail: {self.gmail} || Tarjeta: {self.tarjeta.numeroTarjeta}") 
    
    def __setattr__(self, name, value):
        super().__setattr__(name, value)

    def convertir_dict(self): 
        cliente = {
            "id" : self.id, 
            "nombre" : self.nombreCompleto, 
            "gmail" : self.gmail, 
            "contrasena" : self.contrasena, 
            "tarjeta" : self.tarjeta.convertir_dict(), 
            "carrito" : [self.carrito.convertir_dict()]
        }

        return cliente
    
    def convertir_cliente(self, data): ##data es un obj json 
        self.id = data['id']
        self.nombreCompleto = data['nombre']
        self.gmail = data['gmail']
        self.contrasena = data['contrasena']
        self.tarjeta = Tarjeta(data['tarjeta']['nombre dueño'], 
                                                   data['tarjeta']['codigo seguridad'], 
                                                   data['tarjeta']['numero tarjeta'], 
                                                   data['tarjeta']['dni dueño'], 
                                                   data['tarjeta']['fecha vencimiento'])
        
        return self 
        
        

#####################################################################################################################################
##CLASE TARJETA: contiene los datos de una tarjeta guardada por el cliente, que puede llegar a hacerle uso una vez que decida realizar una compra. 

class Tarjeta: 

    def __init__(self, nombreAutor, codigoSeguridad, numeroTarjeta, dniAutor, fechaVen):
        self.nombreAutor = nombreAutor
        self.codigoSeguridad = codigoSeguridad
        self.numeroTarjeta = numeroTarjeta
        self.dniAutor = dniAutor
        self.fechaVen = fechaVen

    def __str__(self):
        return (f"\n||  Nombre: {self.nombreAutor} ") 
    
    def convertir_dict(self): 
        tarjeta = {
            "nombre dueño" : self.nombreAutor, 
            "codigo seguridad" : self.codigoSeguridad,
            "numero tarjeta" : self.numeroTarjeta,
            "dni dueño" : self.dniAutor, 
            "fecha vencimiento" : self.fechaVen 
        }

        return tarjeta
    
    
#####################################################################################################################################
##CLASE CARRITO : es el conjunto de productos que tiene guardado cada cliente; pueden ser comprados en el momento o comprados despues. 

class Carrito: 

    def __init__(self):
        self.listaProductos = []
        self.total = 0

    def __setTotal__(self):
        for p in self.listaProductos: 
            self.total = self.total + p.precio 

    def agregarProducto(self, producto) :  
        self.listaProductos.append(producto) 
        
    def convertir_dict(self):
        i= 1
        carrito = []

        for p in self.listaProductos: 
            carrito.append(p.convertir_dict())
            i += 1

        return carrito
    
    def mostrarCarrito(self):
        for p in self.listaProductos: 
            print(p) 

    def eliminarProducto(self, nombre): 
        for p in self.listaProductos : 
            if p.nombre == nombre : 
                self.listaProductos.remove(p)
    
#####################################################################################################################################
##CLASE GESTOR CLIENTES: gestiona los clientes que se logean en el sistema 

class GestorClientes: 

    def __init__(self):
        self.listaDeClientes = []
        self.path_archivo = './clientes.json'

    def agregarCliente(self, cliente): 

      if isinstance(cliente, Cliente): 
          self.listaDeClientes.append(cliente)


    def convertir_dict(self) :
        cl = [] 

        for c in self.listaDeClientes: 
            cl.append(c.convertir_dict())

        lc = {'clientes' : cl}

        return lc
    
    def escribirArchivoJson(self):
        with open(self.path_archivo, 'w') as archivo:
            json.dump(self.convertir_dict(), archivo, indent=4)
    
    def leerArchivoClientesJson (self): 
        self.listaDeClientes.clear()
        with open (self.path_archivo, 'r') as archivo: 
            datos = json.load(archivo)
            
            for data in datos['clientes']: 
                cliente = Cliente.convertir_cliente(data)
            
                i=0
                for key in data['carrito'] : 
                     for k in key: 
                         if k['categoria'] == 'Producto Electronico' : 
                             pr = ProductoElectronico(k['id'], 
                                             k['nombre'], 
                                             k['precio'],
                                             k['stock'], 
                                             k['marca'], 
                                             k['categoria'], 
                                             k['tipo'], 
                                             k['modelo'], 
                                             k['almacenamiento'], 
                                             k['tactil'], 
                                             k['cargador'])
                         
                         elif k['categoria']== 'Producto Hogar' : 
                             pr = ProductoHogar(k['id'], 
                                       k['nombre'], 
                                       k['precio'],
                                       k['stock'], 
                                       k['marca'], 
                                       k['categoria'],
                                       k['modelo'], 
                                       k['uso'], 
                                       k['especificacion'])
                         cliente.carrito.agregarProducto(pr)  
                         i = i + 1
                self.listaDeClientes.append(cliente)

    
    def buscarClienteGmail(self, gmail): 

        cli = 0

        for c in self.listaDeClientes: 
            if c.gmail == gmail :
                cli = c 
        
        return cli 
    
    def buscarClienteId (self, id): 

        cli = 0

        for c in self.listaDeClientes: 
            if c.id == id :
                cli = c 
        
        return cli
    
    def getCantClientes (self): 
        return self.listaDeClientes.count 
    
    def eliminarCliente(self, cliente): 

        for c in self.listaDeClientes: 
            if c == cliente : 
                self.listaDeClientes.remove(cliente)
    
    def __str__(self):
        for c in self.listaDeClientes: 
            print(c)

    

#####################################################################################################################################
##CLASE PRODUCTO: metodos y atributos del objeto producto. Super class de otras clases 

class Producto: 

    def __init__(self, id, nombre, precio, stock, marca, categoria):
        self.id = id 
        self.nombre = nombre 
        self.precio = precio 
        self.stock = stock 
        self.marca = marca 
        self.categoria = categoria

    def __str__(self):
        return (f"|| Nombre: {self.nombre}  || Marca: {self.marca}  || Precio: {self.precio}")

    def __setattr__(self, name, value):
        super().__setattr__(name, value)

    def convertir_dict(self): 

        producto = { 
            "id" : self.id, 
            "nombre" : self.nombre, 
            "precio" : self.precio, 
            "stock" : self.stock, 
            "marca" : self.marca, 
            "categoria" : self.categoria
        }

        return producto
    
#####################################################################################################################################
##CLASE PRODUCTO ELECTRONICO: hijo de producto
    
class ProductoElectronico(Producto): 

    def __init__(self, id, nombre, precio, stock, marca, categoria, tipo, modelo, almacenamiento, tactil, cargador):
        super().__init__(id, nombre, precio, stock, marca, categoria)
        self.tipo = tipo
        self.modelo = modelo
        self.almacenamiento = almacenamiento
        self.tactil = f'Es tactil? {tactil}'
        self.cargador = f'Contiene cargador? {cargador}'

    def __str__(self):
        return super().__str__() + (f"|| Modelo: {self.modelo}  || Almacenamiento: {self.almacenamiento}")
    
    def convertir_dict(self):
        pr = super().convertir_dict()

        pr.update({"tipo" : self.tipo, 
                   "modelo" : self.modelo, 
                   "almacenamiento" : self.almacenamiento, 
                   "tactil" : self.tactil, 
                   "cargador" : self.cargador})
        return pr

#####################################################################################################################################
##CLASE PRODUCTO HOGAR: hijo de producto 

class ProductoHogar(Producto): 

    def __init__(self, id, nombre, precio, stock, marca, categoria, modelo, uso, especificacion):
        super().__init__(id, nombre, precio, stock, marca, categoria)
        self.modelo = modelo
        self.uso = uso 
        self.especificacion = especificacion

    def __str__(self):
        return super().__str__() + (f"|| Modelo: {self.modelo}  || Uso: {self.uso}  || Especificacion: {self.especificacion}")
    

    def convertir_dict(self):
        pr = super().convertir_dict()

        pr.update({ "modelo" : self.modelo, 
                    "uso" : self.uso, 
                    "especificacion" : self.especificacion
                   })
        
        return pr

#####################################################################################################################################
##CLASE GESTOR PRODUCTOS: gestiona los distintos productos que el commerce tiene por ofrecer, todos almacenados en un archivo  

class GestorProductos: 

    def __init__(self):
        self.listaProductos = []
        self.path_archivo = './productos.json'
    
    def agregarProducto(self, producto) : 
      if isinstance (producto, Producto): 
          self.listaProductos.append(producto) 

    def getCant(self):
        return len(self.listaProductos) 
    
    def convertir_dict(self) :
        pl = [] 

        for p in self.listaProductos: 
            pl.append(p.convertir_dict())

        lp = {'productos' : pl}

        return lp

    def escribirArchivoJson(self) : 
        with open (self.path_archivo, 'w') as archivo: 
            json.dump(self.convertir_dict(), archivo, indent=4)

    def leerArchivoJson(self): 
        self.listaProductos.clear()
        with open (self.path_archivo, 'r') as archivo: 
            data = json.load(archivo)

            i=1
            print (data)
            for k in data['productos']: 
                if k['categoria'] == 'Producto Electronico' : 
                    pr = ProductoElectronico(k['id'], 
                                             k['nombre'], 
                                             k['precio'],
                                             k['stock'], 
                                             k['marca'], 
                                             k['categoria'], 
                                             k['tipo'], 
                                             k['modelo'], 
                                             k['almacenamiento'], 
                                             k['tactil'], 
                                             k['cargador'])
                    
                elif k['categoria']== 'Producto Hogar' : 
                    pr = ProductoHogar(k['id'], 
                                       k['nombre'], 
                                       k['precio'],
                                       k['stock'], 
                                       k['marca'], 
                                       k['categoria'],
                                       k['modelo'], 
                                       k['uso'], 
                                       k['especificacion'])
                self.listaProductos.append(pr)
                i= i + 1
                    


    def buscarProductoNombre(self, nombre): 
        pr = 0 

        for p in self.listaProductos : 
            if p.nombre == nombre : 
                pr = p 

        return pr
    
    def buscarProductoOrden (self, i): 
        return self.listaProductos[i]   
    
    def eliminarProducto(self, nombre): 

        for p in self.listaProductos : 
            if p.nombre == nombre : 
                self.listaProductos.remove(p)

    def visualizarLista(self):
       for p in self.listaProductos: 
           print(p)
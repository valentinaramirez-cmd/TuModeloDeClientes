from models import GestorClientes, GestorProductos, ProductoElectronico, ProductoHogar, Cliente, Tarjeta, Carrito
from exceptions import DatoInvalidoException, ContrasenaInvalidaException, UsuarioRepetidoException, GmailInvalidoException, GmailRepetidoException
import re

gp = GestorProductos()
gc = GestorClientes()

c = Cliente('lola', 'lol', 'lol', 12)
c1 = Cliente('lolas', 'lol', 'lol', 12)

pr = ProductoHogar(2, 'Juego de sillas', 500000, 25, 'miliffi', 'Producto Hogar', 'nuevas', 'interior', 'material algarrobo')
pr1 = ProductoElectronico(1, 'MOTOG10', 250000, 10, 'motorola', 'Producto Electronico', 'celular', 'g', '128gb', 'si', 'si')


gp.agregarProducto(pr)
gp.agregarProducto(pr1)
gp.escribirArchivoJson()


def verificarEmail (email): 
        pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")

        if not re.fullmatch(pattern, email):
            flag=0
        else:
            flag=1
    
        return flag

def registrarCliente(): 
    print("\n---------------------")
    print("\n  REGISTRAR CLIENTE")
    print("\n---------------------") 

     

    while True: 
        try: 
            print("\nNombre Completo: ") 
            nombreCom= input()

            if not nombreCom: 
                raise DatoInvalidoException
            else: 
                break
        
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato.")


    while True: 
            try: 
                print("\nGmail: ") 
                gmail= input()

                if not gmail: 
                    raise DatoInvalidoException
                else:
                    try: 
                        flag= verificarEmail(gmail)
                        
                        if flag==1 : 
                            try: 
                                flag= gc.buscarClienteGmail(gmail)
                                if flag == 0 : 
                                    break
                                else: 
                                    raise GmailRepetidoException
                            except GmailRepetidoException: 
                                print ("Error. El gmail ya ha sido utilizado") 

                        else: 
                            raise GmailInvalidoException 
                    except GmailInvalidoException: 
                        print ("Error. Ingresar un gmail")
        
            except DatoInvalidoException: 
                print("Error. Es obligatorio ingresar un dato.")

    
    
    while True: 
        try: 
            print("\nContraseña(debe contener minimo 8 caracteres y 1 numero): ")
            contrasena= input()
            
            if not contrasena: 
                raise DatoInvalidoException
            else:  
                try:
                    for c in contrasena: 
                        if c.isdigit() == True:
                            aux = 1
                    if aux == 1:  
                            try: 
                                if len(contrasena) >= 8 : 
                                    break
                                else: 
                                    raise ContrasenaInvalidaException
                            except ContrasenaInvalidaException: 
                                print("Error. La contraseña debe tener al menos 8 caracteres. ") 
                    else: 
                        raise ContrasenaInvalidaException
           
                except: 
                    print("Error. La contraseña debe contener al menos 1 numero. ")
        
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato.")
    
    cliente = Cliente(nombreCom, gmail, contrasena, gc.getCantClientes) 
             
    print("Desea agregar una tarjeta?")
    print("[1] SI")
    print("[2] NO")
    op = int(input())

    if op == 1: 
        tarjeta = registrarTarjeta()
        cliente.__setattr__("tarjeta", tarjeta)
        
    gc.agregarCliente(cliente)


def registrarTarjeta():

    print("\n---------------------")
    print("\n  REGISTRAR TARJETA")
    print("\n---------------------") 

     

    while True: 
        try: 
            print("Ingrese el numero de la tarjeta: ") 
            numeroTarjeta = input()

            if not numeroTarjeta: 
                raise DatoInvalidoException
            else: 
                break
        
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato.")


    while True: 
        try: 
            print("Ingrese el nombre completo del dueño de la tarjeta: ")
            nombreAutor = input()

            if not nombreAutor: 
                raise DatoInvalidoException
            else: 
                break
        
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato.")

    while True: 
        try: 
            print("Ingrese el dni del dueño de la tarjeta: ")
            dniAutor = input()

            if not dniAutor: 
                raise DatoInvalidoException
            else: 
                break
        
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato.")


    while True: 
        try: 
            print("Ingrese el codigo de seguridad: ")
            codSeg = input()

            if not codSeg: 
                raise DatoInvalidoException
            else: 
                break
        
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato.")

    while True: 
        try: 
            print("Ingrese la fecha de vencimiento: ")
            fechaVen = input()

            if not fechaVen: 
                raise DatoInvalidoException
            else: 
                break
        
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato.")

    tarjeta = Tarjeta(nombreAutor, codSeg, numeroTarjeta, dniAutor, fechaVen)

    return tarjeta
   
def registrarProducto(): 

    print("\n---------------------") 
    print("\n  REGISTRAR PRODUCTO")
    print("\n---------------------") 

    while True: 
        try: 
            print("Ingrese el nombre del producto: ") 
            nombrePr = input()

            if not nombrePr: 
                raise DatoInvalidoException
            else: 
                break
        
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato.")
    
    while True: 
        try: 
            print("Ingrese el precio del producto: ") 
            precioPr = input()

            if not precioPr: 
                raise DatoInvalidoException
            else: 
                break
        
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato.")

    while True: 
        try: 
            print("Ingrese el stock del producto: ") 
            stockPr= input()

            if not stockPr: 
                raise DatoInvalidoException
            else: 
                break
        
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato.")

    while True: 
        try: 
            print("Ingrese la marca del producto: ") 
            marcaPr= input()

            if not marcaPr: 
                raise DatoInvalidoException
            else: 
                break
        
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato.")
 
    while True: 
        try: 
            print("Ingrese el tipo de producto: [1] Electronico [2] Hogar") 
            tipoPr= int(input())

            if not tipoPr: 
                raise DatoInvalidoException
            else: 
                if tipoPr == 1 : 
                    prE = ingresarDatosProductoElectronico()
                    producto = ProductoElectronico(1, nombrePr, precioPr, stockPr, marcaPr, 'Producto Electronico', prE.get('tipo'), prE.get('modelo'), prE.get('almacenamiento'), prE.get('tactil'), prE.get('cargador'))
                    break 

                elif tipoPr == 2 : 
                    prH = ingresarDatosProductoHogar()
                    producto = ProductoHogar(1, nombrePr, precioPr, stockPr, marcaPr, 'Producto Hogar', prH.get('modelo'), prH.get('uso'), prH.get('especificacion') )
                    break 

        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato.")

    gp.agregarProducto(producto) 
    gp.visualizarLista()


def ingresarDatosProductoElectronico(): 

    while True: 
        try: 
            print("Ingrese el tipo de producto [1] Celular [2] Notebook [3] Tablet: ") 
            tipoPr = input()

            if not tipoPr: 
                raise DatoInvalidoException
            else: 
                break
        
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato.")
    
    while True: 
        try: 
            print("Ingrese el modelo del producto: ") 
            modeloPr = input()

            if not modeloPr: 
                raise DatoInvalidoException
            else: 
                break
        
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato.")


    while True: 
        try: 
            print("Ingrese el almacenamiento del producto: ") 
            almacenamientoPr = input()

            if not almacenamientoPr: 
                raise DatoInvalidoException
            else: 
                break
        
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato.")


    while True: 
        try: 
            print("Es tactil? [1] si [2] no: ") 
            tactilPr = int(input())

            if not tactilPr: 
                raise DatoInvalidoException
            else: 
                break
        
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato valido.")

    while True:  
        try: 
            print("Incluye cargador? [1] si [2] no: ") 
            cargadorPr = int(input())

            if not cargadorPr: 
                raise DatoInvalidoException
            else: 
                break
        
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato valido.")
    
    prE = { 
        "tipo" : tipoPr,
        "modelo" : modeloPr,
        "almacenamiento" : almacenamientoPr ,
        "tactil" : tactilPr, 
        "cargador" : cargadorPr
    }

    return prE


def ingresarDatosProductoHogar(): 

    while True: 
        try: 
            print("Ingrese el tipo de producto [1] Interior [2] Exterior : ") 
            usoPr = input()

            if not usoPr: 
                raise DatoInvalidoException
            else: 
                break
        
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato.")
    
    while True: 
        try: 
            print("Ingrese el modelo del producto: ") 
            modeloPr = input()

            if not modeloPr: 
                raise DatoInvalidoException
            else: 
                break
        
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato.")
    
    while True: 
        try: 
            print("Incluye cargador? (si, no): ") 
            especificacionPr = input()

            if not especificacionPr: 
                raise DatoInvalidoException
            else: 
                break
        
        except DatoInvalidoException: 
            print("Error. Es obligatorio ingresar un dato valido.")
    
    prH = { 
        "uso" : usoPr,
        "modelo" : modeloPr,
        "especificacion" : especificacionPr
    }

    return prH

def inicioSesionCliente(): 
    print("\n--------------------")
    print("\n   INICIO SESION")
    print("\n--------------------")

    print("\nGmail: ")
    gmail= input()

    flag=gc.buscarClienteGmail(gmail)

    if(flag != 0):
        print("\nContraseña: ")
        contrasena= input() 

        if(contrasena == flag.contrasena): 
            print("\nSesion iniciada. ")
            menuSesionIniciada(flag)
        else: 
             print("\nContraseña incorrecta. ")
    else: 
        print("\nUsuario no existe. ")

def menuSesionIniciada(cliente : Cliente): 

    while True:
        print("\n--------------------")
        print("\n       MENU")
        print("\n--------------------")
        print("\n[ Ingresar Opcion ] \n\n[1] Visualizar productos  \n\n[2] Agregar tarjeta  \n\n[3] Visualizar carrito \n\n[4] Visualizar perfil \n\n[5] Cerrar Sesion")
        print("\n--------------------")

        op=int(input()) 

        if op == 1 : 
            print(gp.visualizarLista())

            print("Desea agregar algun producto al carrito? [1] si [2] no: ")
            opp = int(input())

            if opp == 1 : 
                print("Ingrese el numero del producto: ")
                pr = int(input())

                producto = gp.buscarProductoOrden(pr-1)

                cliente.carrito.agregarProducto(producto)

        elif op == 2 : 
            tarjeta = registrarTarjeta()
            cliente.__setattr__("tarjeta", tarjeta)
        elif op == 3 : 
            print(cliente.carrito.mostrarCarrito())
            print('Desea comprar? [1] si [2] no:')
            oppp = int(input())

            if oppp == 1: 
                while True: 
                    listaCompra = []
                    listaCompra.append(realizarCompra())
                    print('Seguir comprando?[1] si [2] no:')
                    o = int(input())
                    if o == 2: 
                        print('Compra finalizada. Los productos comprados: ')
                        for a in listaCompra: 
                            print(a)
                    
        elif op == 4 : 
            print(cliente)
        elif op == 5 : 
            print('Sesion cerrada. ')
            gc.escribirArchivoJson()

def menuCliente(): 

    while True :
        print("\n--------------------")
        print("\n       MENU")
        print("\n--------------------")
        print("\n[ Ingresar Opcion ] \n\n[1] Iniciar Sesion  \n\n[2] Registrar Usuario")
        print("\n--------------------")

        op=int(input())

        if op == 1 : 

            inicioSesionCliente()
        elif op == 2 : 
            registrarCliente()
        else : 
            print("\nLa opcion ingresada es incorrecta. Para volver al menu ingresar 1.")
    

def realizarCompra(cliente : Cliente) : 
    
    print('Ingrese el numero del producto a comprar: ')
    op = int(input())

    pr = gp.buscarProductoId(op)

    cliente.carrito.eliminarProducto(pr.nombre)

    return pr 

        

menuCliente()
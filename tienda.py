
def crear_producto():
    nombre_P=input('ingrese el nombre del producto\n=>')
    while True:
        try:
            stock=int(input('ingrese el stock del producto\n=>'))
            precio_P=int(input('ingrese el precio del producto\n=>'))
        except ValueError:
            print('En el stock y en el precio solo se aceptan numero enteros')
        else:
            if precio_P<=0 or stock<=0:
                print('el stock y el precio deben ser mayor a 0')
            else:
                producto=[nombre_P,stock,precio_P]
                return producto
productos=[]
productos2=[]         
def registrar_P(producto):
    for P_guardado in productos:
        if P_guardado[0]==producto[0]:
            P_guardado[1]+=producto[1]
            P_guardado[2]=producto[2]
            return
    
    productos.append(producto)

def comprar_producto(nombre_producto,cantidad):
    
    for producto in productos:
        if producto[0] == nombre_producto:
            while True:
                try:
                    cantidad
                except ValueError:
                    print('La cantidad debe ser un número entero')
                else:
                    if cantidad <= 0:
                        print('La cantidad debe ser mayor a 0')
                    elif cantidad > producto[1]:
                        print('No hay suficiente stock para esa cantidad')
                    else:
                        precio=cantidad*producto[2]
                        break
            
            while True:
                try:
                    pago=int(input('Ingrese la cantidad de dinero con la que pagara\n=>'))
                except ValueError:
                    print('El pago deben ser en números enteros')
                else:
                    if pago<precio or pago<=0:
                        print("Disculpe se requiere mas dinero para la compra")
                    elif pago>precio:
                        vuelto=pago-precio
                        producto[1] -= cantidad
                        print("La compra se ha realizado con exito")
                        print(f'Ha comprado {cantidad} unidades de {nombre_producto}, su vuelto es de ${vuelto}')
                        return 
                    elif pago==precio:
                        producto[1] -= cantidad
                        print("La compra se ha realizado con exito")
                        print(f'Ha comprado {cantidad} unidades de {nombre_producto}')
                        return 
        else:
            print('El producto no está registrado en la tienda')
    
print("Bienvenido a la tienda")

while True:
    while True:
        print("Escoja una de las siguientes opciones:")
        print("1)Vender Producto")
        print("2)Ver Productos")
        print("3)Comprar productos")
        print("4)Salir de la tienda")
        try:
            opc_MP=int(input('=>'))
        except ValueError:
            print("la opciones solo aceptan valores nomericos")
        else:
            if opc_MP<=0 or opc_MP>=5:
                print("las opciones del menu no pueden ser menores\nni mayores en compracion con las opciones dadas")
            else:
                break
    match opc_MP:
        case 1:
            producto=crear_producto()
            registrar_P(producto)
        case 2:
            if productos==productos2:
                print("""No hay productos registrados en la tienda,porfavor\nregistre nuevos productos para vender""")
            elif productos!=productos2:
                print("   producto - stock - precio  ")
                for i in range(0,len(productos)):
                    print(f'{i+1}.- {productos[i]}')
                    
        case 3:
            if productos==productos2:
                print("No hay productos a la venta lo sentimos")
            elif productos!=productos2:
                comprar_producto('play',2)
        
        case 4:
            print("hasta luego, gracias por su \npreferencia de compra y venta")
            break
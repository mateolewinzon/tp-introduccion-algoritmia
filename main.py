def BuscarMinimo(lista):
    minimo = lista[0]
    indices_minimos = [0]
    for i in range(len(lista)):
        if lista[i] < minimo:
            minimo=lista[i]
            indices_minimos = [i]
        elif lista[i] == minimo and i != 0:
            indices_minimos.append(i)
    return indices_minimos

def BusquedaBinaria(lista, x): # Solo se puede utilizar si la lísta está previamente ordenada 
    LI=0
    LS=len(lista)-1
    pos=(LI+LS)//2
    while (LS >=LI and lista[pos] != x):
        if x > lista[pos]:
            LI=pos+1
        else:
            LS=pos-1
        pos=(LI+LS)//2
    if LS < LI :
        pos=-1

    return pos

def OrdenarPorInsercion(lista): 
    n=len(lista)
    for i in range(1,n):
        desordenado=lista[i]
        c=i
        while (c >0 and lista[c-1] > desordenado):
            lista[c]=lista[c-1]
            c-=1
        lista[c]=desordenado

# 1. Cargar clientes

clientes = []

nro_cliente = int(input('Ingrese número de cliente '))
while nro_cliente != 0:
    clientes.append(nro_cliente)
    nro_cliente = int(input('Ingrese número de cliente '))

OrdenarPorInsercion(clientes)

# 2. Ingresar ventas 

ventas = [] # Indice de lista cliente = ventas del cliente
for i in clientes: 
    ventas.append(0)

buscar_cliente =  int(input('Buscar cliente '))
while buscar_cliente != -1:
    cliente_encontrado = -1
    while cliente_encontrado == -1:
        # Buscar cliente
        cliente_encontrado = BusquedaBinaria(clientes, buscar_cliente)
        if cliente_encontrado == -1: 
            print('Cliente inválido')
            buscar_cliente =  int(input('Buscar cliente '))   
    venta = int(input("Ingrese venta: "))
    while venta != -1:
        ventas[cliente_encontrado]+=venta
        venta = int(input("Ingrese venta: "))
    buscar_cliente =  int(input('Buscar cliente '))

#Cliente(s) con venta mínima
indices_con_min_venta = BuscarMinimo(ventas)
for i in indices_con_min_venta: 
    print('Cliente con ventas mínimas: ', clientes[i])

# ventas totales

# lista de clientes
print(clientes, ventas)
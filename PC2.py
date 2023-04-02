# EJERCICIO 1

print("SELECCIONE UNA OPCION:")

print("1. DIBUJAR CUADRADO")
print("2. IDENTIFICAR MÚLTIPLO DE 2")
print("3. ENTREGAR LISTA DE MAYORES DE EDAD")

opcion=int(input())

if opcion>3:
    print("INGRESE UN NUMERO VALIDO - CORRA EL CODIGO DE NUEVO")
    

elif opcion==1:
    print("INGRESE EL AREA DEL CUADRADO")
    
    area=int(input())
    print(" ")
    for x in range(area):
        if x==0:
            print("*"*area*2)
        elif x==area-1:
            print("*"*area*2)
        else:
            print("*"+" "*(area*2-2)+"*")


elif opcion==2:
    print("INGRESE EL NÚMERO")
    numero=int(input())
    print("")
    if str(float(numero/2)).split(".")[1]=="5":
        print("NO ES MULTIPLO DE 2")
    else:
        print("ES MULTIPLO DE 2")
    
elif opcion==3:

    lista_personas=[]

    print("CUANTAS PERSONAS SON?")

    for x in range(int(input())):
        print("INGRESE NOMBRE DE PERSONA {}".format(x+1))
        nombre=str(input())
        print("INGRESE EDAD DE PERSONA {}".format(x+1))
        edad=int(input())

        lista_personas.append([nombre,edad])
    print("")
    print("PERSONAS MAYORES DE EDAD:")
    for x in lista_personas:
        if x[1] >= 18:
            print(str(x[0])+" - "+str(x[1])+" AÑOS")




# Ejercicio 2

libros=["LA ODISEA","LOS MISERABLES","MOBY DICK"]

autores=["HOMERO","VICTOR HUGO","HERMAN MELVILLE"]

categorias=["MITOLOGÍA GRIEGA","LITERATURA FRANCESA","LITERATURA NORTEAMERICANA"]

estado=["DISPONIBLE","DISPONIBLE","PRESTADO"]

usuarios=["VALERIA","LUCIANO","MATIAS","MARTIN","VICTOR"]

biblioteca={
 "libro1":{"libro":libros[0],"autor":autores[0],"categoria":categorias[0],"estado":estado[0]},
 "libro2":{"libro":libros[1],"autor":autores[1],"categoria":categorias[1],"estado":estado[1]},
 "libro3":{"libro":libros[2],"autor":autores[2],"categoria":categorias[2],"estado":estado[2]},
 "usuarios":usuarios
}

print("SELECCIONAR LIBRO:")
print("")
n=0
for x in biblioteca:
    n+=1
    if x.startswith("libro"):
        print("{})".format(n),biblioteca[x]["libro"])
    
lib=int(input())

print("")
print("SELECCIONE UNA OPCION:")
print("1) MOSTRAR AUTOR")
print("2) MOSTRAR CATEGORIA")
print("3) MOSTRAR ESTADO")
print("4) TOMAR PRESTADO")

lib2=int(input())

print("")
for x in biblioteca:
    if str(lib) in x:
        if lib2==1:
            print(biblioteca[x]["autor"])
        if lib2==2:
            print(biblioteca[x]["categoria"])
        if lib2==3:
            print(biblioteca[x]["estado"])
        if lib2==4:
            
            if biblioteca[x]["estado"]=="PRESTADO":
                print("NO ESTÁ DISPONIBLE")
            else:
                biblioteca[x]["estado"]="PRESTADO"
                print("Listo!")
                print("")
                print(biblioteca[x])

                
                
                
# Ejercicio 3

def mayor(x,y):
    if x>y:
        return x
    elif y>x:
        return y
    else:
        return x
    
mayor(5,2)



import os
# Ejercicio 5 
def subcarpetas(m):
    if m==0:
        print("Archivos:")
        for x in list(os.walk(os.getcwd()))[0][2]:
            print(x)
        print("")
        print("")
        print("Subcarpetas:")
        for x in list(os.walk(os.getcwd()))[0][1]:
            print(x)
    
    if m==1:
        for x in range(len(list(os.walk(os.getcwd()))[0][1])):
            print(list(os.walk(os.getcwd()))[x+1][0])
            print("Archivos:")
            print(list(os.walk(os.getcwd()))[x+1][2])
            print("Subcarpetas:")
            if len(list(os.walk(os.getcwd()))[x+1][1]) == 0:
                print("No hay subcarpetas")
            else:
                print(list(os.walk(os.getcwd()))[x+1][0])
            print("")
    
def subcarpetas2():
    m=0
    subcarpetas(m)
    print("")
    print("Imprimir archivos de subcarpetas:")
    
    print("1) Si")
    print("2) No")
    
    m=int(input())
    
    print("")
    if m==1:
        subcarpetas(m)
    else:
        pass

subcarpetas2()




# Ejercicio 7

texto='Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.'

# Separar palabras por espacio
lista_texto=texto.split(" ")

print(lista_texto)
print("")

# Volver todo el texto en mayúscula
texto2=""
for x in lista_texto:
    texto2+=x.upper()
    texto2+=" "

print(texto2[:-1])
print("")

# Volver todo el texto en minúscula
texto2=""
for x in lista_texto:
    texto2+=x.lower()
    texto2+=" "

print(texto2[:-1])
print("")




# Ejercicio 8

def primo(numero):
    divisores=0
    for x in range(numero):
        if str((numero/(x+1))).split(".")[1]=="0":
            divisores+=1
    
    if divisores==2:
        return "p"
    else:
        return "np"

def primo2(numero):
    if 10**5>=numero:
        primos=[]
        for x in range(numero):
            if primo(x+1)=="p":
                primos.append(x+1)
        return primos
    else:
        return "Numero muy alto"
        
        
primo2(50)




# Ejercicio 9

### Minisistema
roles=['admin','vendedor','inventario']

sistema={
    "nombre":"tienda",

    "usuarios":[{'name':"",
                 'password':"",
                 'rol':"" }],##vendedor ,administrador ,inventario
    
    "sedes":[{"nombreSede":"",
              "ubicacion":""}],
    
    "productos":[{"nombre":"manzana","precio":3,"stock":3},
                {"nombre":"pera","precio":2,"stock":4},
                {"nombre":"uva","precio":2,"stock":5}]
}
##### funciones
## karen vera
def agregarUsuario():
    nameUsuario=input("ingrese el nombre de usuario")
    password=input("ingrese su password")
    while True:
        rol=input("ingrese su rol")
        if rol in roles:
            break
        else:
            print("ingrese un rol correcto",roles)
    
    dictUser={
        'name':nameUsuario,
        'password':password,
        'rol':rol
    }
    sistema['usuarios'].append(dictUser)
###
def eliminarUsuario():
    usuarioPorEliminar=input("ingrese usuario por eliminar")
    for i,valor in enumerate(sistema['usuarios']):
        if valor['name']==usuarioPorEliminar:
                ## ingresar password para verificar que es correcto
                sistema['usuarios'].remove(i)
    ## remove
    pass
###
def obtenerRol(usuario):
    rol=""
    for i,valor in enumerate(sistema["usuarios"]):
        if valor['name']==usuario:
            rol=valor['rol']
    return rol
####
def agregarSedes():
    usuario=input("ingresa usuario")
    rol=obtenerRol(usuario)
    if rol=='admin':
        sede=input("ingrese sede")
        ubicacion=input("ingrese ubicacion")
        dictSede={
            'sede':sede,
            'ubicacion':ubicacion
        }
        sistema["sedes"].append(dictSede)
    else:
        print("no es un rol permitido")
###
def verSedes():
    pass
#####

def agregarProductos():
    print("Ingrese nombre del producto:")
    nomb_p=str(input())
    print("Ingrese precio del producto:")
    prec_p=float(input())
    print("Ingrese stock del producto:")
    stock_p=int(input())
    
    sistema["productos"].append({"nombre":nomb_p,"precio":prec_p,"stock":stock_p})
    
####
def cambiarStock():
    print("Seleccione un producto:")

    lista_prodc=[]
    kn=0
    for x in sistema["productos"]:
        kn+=1
        print("{})".format(kn),x["nombre"])
        lista_prodc.append(x["nombre"])


    opc1=int(input())

    print("")
    print("Stock actual: {}".format(sistema["productos"][opc1-1]["stock"]))
    print("Stock nuevo:")
    opc2=int(input())

    sistema["productos"][opc1-1]["stock"]=opc2
    print("Listo!")

cambiarStock()


print(sistema)
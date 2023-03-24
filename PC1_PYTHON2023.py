# Ejercicio 1 
print("dame tu nombre")
nombre=str(input("dame tu nombre"))
print("dame tu apellido")
apellidos=str(input("dame tus apellidos"))
print(nombre+apellidos)

# ejercicio 2
pi=3.14
print("radio del círculo")
r=float(input()) ## aquí se ingresará el valor del radio
a=pi * (r * r)

print("áera del cuadrado")
l=int(input()) # valor del lado del cuadrado
c=l*l

print("área del triángulo") 
b=float(input()) #valor de la base del triangulo
h=float(input()) #valor de la altura del triangulo
t=(b*h)/ 2

#Ejercicio 3
a=2
b=3
c=6
suma=a+b+c
resta=c-b-a
multiplicación=a*b*c
división=a/c
división_entera=int(b/a)

#Ejercicio 4
hola={"hola",1}
type(hola)

#Ejercicio 5
import sys
variable = sys.argv[0]
print(variable)

#Ejercicio 6
lista=[]

for x in range(int(input())):
    lista.append(x+1)
    
sum(lista)
#Ejercicio 7
num1=int(input())
num2=int(input())

print("")
print("Iguales:")
print(num1==num2)
print("")
print("Diferentes:")
print(num1!=num2)
print("")
print("Mayor:")
print(num1>num2)
print("")
print("Menor:")
print(num1<=num2)

#Ejercicio 8
print("Crear contraseña:")
contraseña=str(input())

print("")

print("Escribir nuevamente contraseña:")
contraseña2=str(input())

if contraseña2==contraseña:
    print("Coincide")
else:
    print("No coincide")

#Ejercicio 9
listap=[("Luciano",19,"vacio"),("Valeria",21,1801),("Diego",13,1773),("Valentino",12,1834)]
listap2=[]

for x in listap:
    if x[1]>=18:
        if type(x[2])==int:
            listap2.append(x)
        
print(listap2)

#ejercicio 10
cursos={"nombre de curso" : str(input()), 
 "cantidad de alumnos" : int(input()), 
 "activo" : True, 
 "nombre de profesor" : str(input()),
 "max nota" : int(input()),
 "alumnos" : ["Valeria","Alonso","Luciano","Lucía"]}

print(cursos)

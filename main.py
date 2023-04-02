import random
import requests


__name__=="__main__"

class Sorteo:
    maxim=15
    listan=[]
    cant_num=3
    
    def __init__(self, name):
        self.name = name
    
    def agregar_numeros(self):
        for x in range(self.cant_num):
            print("Numero {}".format(x+1))
            y=int(input())
            if self.maxim >= y:
                self.listan.append(y)
            else:
                print("No puede ingresar numeros mayores a {}".format(self.maxim))
        
    def lista_num(self):
        return self.listan
    
    def sorteo(self):
        return random.choice(self.listan)

def poke_random():
    r = requests.get("https://pokeapi.co/api/v2/pokedex/1/")

    datos=r.json()

    # Dame un pokemon aleatorio

    return datos["pokemon_entries"][random.randint(0,1010)]

from datetime import datetime

class Registro:
    inp=[""]
    namefile='readme.txt'
    
    def __init__(self, name):
        self.name = name
    
    def input1(self):
        print("ingrese input")
        self.inp[0] = str(input())
    
    def guardar_archivo(self):
        with open(self.namefile, 'w') as f:
            f.write('{}-{}-{}'.format(datetime.now(),self.namefile,self.inp[0]))
    
    def leer_archivo(self):
        with open('readme.txt') as f:
            lines = f.readlines()
        return lines
    
def validar_num(x):
    if str(x).startswith("9") and (len(str(x))==9):
        print("Validado!")
    else:
        print("Ingrese un numero valido")
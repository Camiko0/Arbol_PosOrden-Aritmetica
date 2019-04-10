from pila import *
from arbol import *

class Arbol:

    """ CREAR EL ARBOL """
    def __init__(self):
        pila = Pila()
        
    """ CREAR EL ARBOL """ 
    def convertir(self,lista, pila):
        if lista != []:
            if lista[0] in "+-*/":
                nodo_der = pila.desapilar()
                nodo_izq = pila.desapilar()
                pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
            else:
                pila.apilar(Nodo(lista[0]))
            return self.convertir(lista[1:],pila)
                

    """ EVALUAR EL ARBOL CREADO """ 
    def evaluar(self,arbol):
        if arbol.valor == "+":
            return self.evaluar(arbol.izq) + self.evaluar(arbol.der)
        if arbol.valor == "-":
            return self.evaluar(arbol.izq) - self.evaluar(arbol.der)
        if arbol.valor == "/":
            return self.evaluar(arbol.izq) / self.evaluar(arbol.der)
        if arbol.valor == "*":
            return self.evaluar(arbol.izq) * self.evaluar(arbol.der)
        return int(arbol.valor)


    


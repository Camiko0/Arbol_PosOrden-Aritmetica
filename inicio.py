# -*- coding: utf-8 -*-
from pila import *
from arbol_expresiones import *

class Inicio:

    """ INSTANCIAS """
    def __init__(self):
        self.arbol = Arbol()
        self.pila = Pila()

    """ AGREGAR ELEMENTOS A LA COLA """
    def abrir_archivo(self):
        #Abrir .txt con expresiones aritmeticas
        expresiones = open("expresiones.txt")
        linea = [" "]
        impresion = ''
        while linea != '':
            #Leer linea a linea del .txt
            linea = expresiones.readline().split(' ')
            if (linea == ['']):
                expresiones.close()
                break
            #Se envia una a una cada expresión del archivo
            self.arbol.convertir(linea[:-1], self.pila)
            #Resultado para el archivo
            impresion += "La respuesta para ["+' '.join(map(str, linea[:-1])).strip('[]')+"] es: "+str(self.arbol.evaluar(self.pila.desapilar()))+'\n'
        return impresion

    """ AGREGAR EL RESULTADO AL ARCHIVO """   
    def escribir_archivo(self,resultado):
        busquedas = open("resultados.txt", "w")
        busquedas.write(resultado)
        busquedas.close()

inicio = Inicio()
salida = inicio.abrir_archivo()
inicio.escribir_archivo(salida)

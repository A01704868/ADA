# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 17:26:40 2021

@author: alexd
"""
def parentesis(entrada):
    #utilizar una lista como pila FILO
    pila = []
    #iterar a lo largo de todo el string; char es el caracter
    for char in entrada:
        #si char es igual a una llave abierta, push a la pila
        if char == "(" or char == "[":
            pila.append(char)
        #en caso de que se meta una llave cerrada primero
        elif len(pila) == 0:
            if char == ")" or char == "]":
                print("La secuencia no es valida")
                return
        #si se introduce una llave cerrada, la llave en la cima de la pila debe ser la abierta
        elif char == "]" and pila[-1] == "[":
            pila.pop()        
        elif char == ")" and pila[-1] == "(":
            pila.pop()
        else:
            print("La secuencia no es valida")
            return
    # solo se valida si se llega a este punto y la pila esta vacia
    if len(pila) == 0:
        print("La secuencia es valida")
    else:
        print("La secuencia no es valida")

entrada = "([])[]()"
parentesis(entrada)
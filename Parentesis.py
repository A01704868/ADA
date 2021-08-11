# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 17:26:40 2021

@author: alexd
"""
def parentesis(entrada):
    pila = []
    for char in entrada:
        if char == "(" or char == "[":
            pila.append(char)
        elif len(pila) == 0:
            if char == ")" or char == "]":
                print("La secuencia no es valida")
                return
        elif char == "]" and pila[-1] == "[":
            pila.pop()        
        elif char == ")" and pila[-1] == "(":
            pila.pop()
        else:
            print("La secuencia no es valida")
            return
    if len(pila) == 0:
        print("La secuencia es valida")
    else:
        print("La secuencia no es valida")

entrada = "([])[]()"
parentesis(entrada)

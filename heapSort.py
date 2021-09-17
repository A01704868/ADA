# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 12:32:36 2021

@author: alexd
"""

def heapify(array,n, i):
    maximo = i
    izquierda = 2*i + 1
    derecha = 2*i + 2
    
    if  izquierda < n and array[maximo] < array[izquierda]:
        maximo = izquierda
    
    if derecha < n and array[maximo] < array[derecha]:
        maximo = derecha
        
    if i != maximo:
        array[i], array[maximo] = array[maximo], array[i]
        heapify(array, n, maximo)

def heapSort(array):
    n = len(array)
    #range(start, stop , step)
    #// quita digitos despues del decimal
    for i in range(n//2 - 1,-1,-1):
        heapify(array,n,i)
        
    for i in range(n-1, 0 , -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)

array = [87,51,45,60,101,81,77,33]

heapSort(array)
n = len(array)
for i in range(n):
    print(array[i])
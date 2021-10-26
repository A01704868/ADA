# -*- coding: utf-8 -*-
"""
@author: alexd
"""

import numpy as np

class Grafo:
    
    def __init__(self,vertices,aristas):
        self.vertices = vertices
        self.aristas = aristas
        self.matriz = np.zeros(shape=(vertices,vertices))
        
    def agregarArista(self,i,j):
        self.matriz[i][j] = 1
        self.matriz[j][i] = 1
    
    def dfs(self, x, y):
        print(x, end = ' ')
        y[x] = True
        
        for i in range(self.vertices):
            if self.matriz[x][i] == 1 and not y[i]:
                self.dfs(i,y)

vertices, aristas = 7, 7

a = Grafo(vertices,aristas)
a.agregarArista(0,1)
a.agregarArista(1,1)
a.agregarArista(0,2)
a.agregarArista(2,2)
a.agregarArista(3,3)
a.agregarArista(4,4)
a.agregarArista(0,5)
a.agregarArista(5,5)
a.agregarArista(0,6)
a.agregarArista(6,6)
print(a.matriz)

b = vertices * [False]

a.dfs(0, b)
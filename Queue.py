# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 08:50:35 2021

@author: alexd
"""

class Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def agregar(self,item):
        self.stack1.append(item)
    
    def quitar(self):
        if len(self.stack2) == 0:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
        
        return self.stack2.pop()
    
x = Queue()
x.agregar(45)
x.agregar(51)
x.agregar(60)
x.agregar(77)
print(x.stack1)
print(x.quitar())
print(x.stack2)
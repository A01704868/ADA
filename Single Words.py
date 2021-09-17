# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:19:30 2021

@author: alexd
"""

words = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

splitWords = words.split()

splitWords = set(splitWords)

print(' '.join(splitWords))
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:51:24 2018

@author: atc00099
"""

farm_animals = ['cow', 'pig', 'horse']
domestic_animals = ['dog', 'cat', 'gold fish']
zoo_animals = ['lion', 'elephant', 'gorilla']
animals = farm_animals + domestic_animals + zoo_animals
for index_value in range(len(animals)):
    print("{0:d}:{1!s}".format(index_value, animals[index_value]))

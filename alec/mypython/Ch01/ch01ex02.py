# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:04:41 2018

@author: atc00099
"""

animals_dictionary = {}
animals_list = ['cow', 'pig', 'horse']
other_list = [4567,[4,'turn',7,'left'],'Animals are great.']
for index_value in range(len(animals_list)):
    if animals_list[index_value] not in animals_dictionary:
        animals_dictionary[animals_list[index_value]] = other_list[index_value]
for key, value in animals_dictionary.items():
    print("{0!s}:{1}".format(key,value))        
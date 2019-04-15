# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:37:51 2018

@author: atc00099
"""

list_of_lists = [['cow', 'pig', 'horse'],['dog', 'cat', 'gold fish'],\
                 ['lion', 'elephant', 'gorilla']]
for animals_list in list_of_lists:
    max_index = len(animals_list)
    output = ''
    for index in range(len(animals_list)):
        if index < (max_index-1):
            output += str(animals_list[index])+','
        else:    
            output += str(animals_list[index])+'\n'
    print(output)        
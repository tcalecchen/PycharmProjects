#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:00:13 2018

@author: atc00099
"""

#讀取檔案
#讀取一個文字檔
import sys

input_file = sys.argv[1]

print("Output #143: ")

filereader = open(input_file, 'r')
for row in filereader:
    print(row.strip())
filereader.close()      

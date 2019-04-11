#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:00:13 2018

@author: atc00099
"""
from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import sys
import glob
import os

# READ A FILE
# Read a single text file

#input_file = sys.argv[1]

#print("Output #143: ")
#filereader = open(input_file, 'r')
#for row in filereader:
#    print(row.strip())
#filereader.close()      


#input_file = sys.argv[1]
#print("Output #144")
#with open(input_file, 'r', newline='') as filereader:
#  for row in filereader:
#    print("{}".format(row.strip()))

# 讀取多個文字檔
#print("Output #145")
#inputPath = sys.argv[1]      
#for input_file in glob.glob(os.path.join(inputPath,'*.txt')):
#    with open(input_file, 'r', newline='') as filereader:
#        for row in filereader:
#            print("{}".format(row.strip()))
            
#寫入檔案
#寫入文字檔

my_letters = ['a','b','c','d','e','f','g','h','i','j']
max_index = len(my_letters)
output_file = sys.argv[1]
filewriter = open(output_file, 'w')
for index_value in range(max_index):
    if index_value < (max_index-1):
        filewriter.write(my_letters[index_value]+'\t')
    else:                
        filewriter.write(my_letters[index_value]+'\n')
filewriter.close()
print("Output #146: Output written to file")       
      
      
#寫到一個 CSV 檔
my_numbers = [0,1,2,3,4,5,6,7,8,9]     
max_index = len(my_numbers)
output_file = sys.argv[1]
filewriter = open(output_file, 'a') 
for index_value in range(max_index):
    if index_value < (max_index-1):
        filewriter.write(str(my_numbers[index_value])+',')
    else:                
        filewriter.write(str(my_numbers[index_value])+'\n')
filewriter.close()
print("Output #147: Output append to file")             
      
      
      
      
      
      
      
      
      
      
      
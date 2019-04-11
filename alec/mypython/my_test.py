#!/usr/bin/env python3
from math import exp, log, sqrt
import re
from datetime import date, datetime, timedelta
from operator import itemgetter
import sys
import glob
import os

# Print a simple string
from typing import List


# READ A FILE
# Read a single text file
#input_file = sys.argv[1]

## Read a text file (older method) ##
#print("Output #141:")
#filereader = open(input_file, 'r', newline='')
#for row in filereader:
#	print("{}".format(row.strip()))
#filereader.close()

## Read a text file (newer method) ##
#print("Output #142:")
#with open(input_file, 'r', newline='') as filereader:
#	for row in filereader:
#		print("{}".format(row.strip()))

print("Output #143:")
# READ MULTIPLE FILES
# Read multiple text files
inputPath = sys.argv[1]  # 存特定資料夾路徑
# os.path.join 函式會將這個資料夾路徑與資料夾中所有符合特定文字組合的檔案名稱結合
# 並用 glob.glob 函式回傳串列
for input_file in glob.glob(os.path.join(inputPath, '*.txt')):
    with open(input_file, 'r', newline='') as filereader:
       for row in filereader:  # for 迴圈的內文會印出每一列
           print("{}".format(row.strip()))  # strip 函式會在印出每一列之前，將每列結尾的空格、tab
                                            # 與換行字元移除

# WRITE TO A FILE
# Write to a text file
my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
max_index = len(my_letters)
output_file = sys.argv[1]
filewriter = open(output_file, 'w')
for index_value in range(len(my_letters)):
    if index_value < (max_index-1):
        filewriter.write(my_letters[index_value]+'\t')
    else:
        filewriter.write(my_letters[index_value]+'\n')
filewriter.close()
print("Output #144: Output written to file")

# Write to a CSV file
#my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#max_index = len(my_numbers)
#output_file = sys.argv[1]
#filewriter = open(output_file, 'a')
#for index_value in range(len(my_numbers)):
#    if index_value < (max_index-1):
#        filewriter.write(str(my_numbers[index_value])+',')
#    else:
#        filewriter.write(str(my_numbers[index_value])+'\n')
#filewriter.close()
#print("Output #145: Output appended to file")

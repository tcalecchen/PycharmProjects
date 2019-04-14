#!/usr/bin/env python3  # 註解，讓腳本可以跨作業系統傳遞
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as filereader:  # 將 input_file 開成一個檔案物件 filereader，'r' 指定讀取模式，
                                                       # 也就是說， input_file 會被開啟來讀取
    with open(output_file, 'w', newline='') as filewriter: # 將 output_file 開成一個檔案物件 filewriter，'w' 指定寫入模式，
                                                           # 也就是說， output_file 會被開啟來寫入。
                                                           # 它會在陳述式結束時，自動關閉檔案物件
        header = filereader.readline()  # 讀取輸入檔的第一行，並將它以字串格式指派給變數 header
        header = header.strip()         # 用 string 模組的 strip 函式來移除標題字串兩端的空格、tab與換行字元，並再次將
                                        # 移除後的版本指派給變數 header
        header_list = header.split(',') # 用 string 模組的 split 函式來用逗號分解字串，放入串列，串列內的每個值都是一個
                                        # 欄位標題，並將串列指派給 header_list 變數
        print(header_list)
        filewriter.write(','.join(map(str, header_list))+'\n') # 用 filewriter 物件的 write 方法將 header_list 內的每
                                                               # 一個值寫到輸出檔
        # map 函式會對 header_list 內的每一個值套入 str 函式，來確保每個值都是字串。接著 join 會在 header_list 的每一個值
        # 之間插入逗號，將串列轉成字串。接著將一個換行字元加到字串的結尾。最後，filewriter 物件將字串寫到輸出檔第一列。
        for row in filereader:  # 建立一個 for 迴圈來迭代輸入檔其餘的資料列
            row = row.strip()   # 使用 strip 函式來移除標題字串兩端的空格、tab與換行字元，並將移除後的版本再次指派給 row。
            row_list = row.split(',')  # 用 split 函式來用逗號分解字串，放入串列，串列內的每個值都是一個資料列的欄位值，
                                       # 並將串列指派給 row_list 變數
            print(row_list)
            filewriter.write(','.join(map(str, row_list))+'\n')  # 將值寫至輸出檔
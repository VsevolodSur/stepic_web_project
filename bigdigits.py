#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys

Zero = [" *** ",
        "*   *",
        "*  **",
        "* * *",
        "**  *",
        "*   *",
        " *** "]

One  = ["  *  ", 
        " **  ", 
        "* *  ", 
        "  *  ", 
        "  *  ", 
        "  *  ", 
        " *** "]

Two  = [" *** ", 
        "*   *", 
        "*   *", 
        "   * ", 
        "  *  ", 
        " *   ", 
        "*****"]

Three = [" *** ", 
         "*   *", 
         "    *", 
         "  ** ", 
         "    *", 
         "*   *", 
         " *** "]

Four  = ["*   *", 
         "*   *", 
         "*   *", 
         " ****", 
         "    *", 
         "    *", 
         "    *"] 

Five  = [" ****", 
         "*    ", 
         "*    ", 
         " *** ", 
         "    *", 
         "*   *", 
         " *** "]

Six   = [" *** ", 
         "*    ", 
         "*    ", 
         "**** ", 
         "*   *", 
         "*   *", 
         " *** "]

Seven = ["*****", 
         "    *", 
         "    *", 
         "   * ", 
         " *   ", 
         "*    ", 
         "*    "]

Eight = [" *** ", 
         "*   *", 
         "*   *", 
         " *** ", 
         "*   *", 
         "*   *", 
         " *** "]  

Nine =  [" *** ", 
         "*   *", 
         "*   *", 
         " ****", 
         "    *", 
         "    *", 
         " *** "]        

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]
print("")
try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            # print (column)
            number = int(digits[column])
            digit = Digits[number]
            line += digit[row] + " "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)

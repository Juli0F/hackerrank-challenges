#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    pts = [0, 0]
    if len(a) != len(b):
        return "Invalid input"
    for i in range(0, len(a)):
        if b[i] > a[i]:
            pts[1] += 1
        elif b[i] < a[i]:
            pts[0] += 1
    print(pts)


def diagonalDifference(arr):
    left_right = 0
    righ_left = 0
    if len(arr[0]) >= -100 and len(arr[0]) <= 100:
        for i in range(len(arr)):


            while len(arr[i]) != len(arr):
                arr[i].append(0)

            for j in range(len(arr)):
                if i == j:

                    left_right += arr[i][j]
                if j == len(arr[i])-1:
                    righ_left += arr[i][j-i]

    return abs(left_right - righ_left)

def staircase(n):
    for i in range(n):
        print(" "*(n-i-1) + "#"*(i+1))
    return ""

def miniMaxSum(arr):
    # Write your code here
    lst = []
    temp = arr[0]
    aux = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] > arr[j]:
                aux = arr[i]
                arr[i] = arr[j]
                arr[j] = aux
    result = 0
    for i in arr:
        result += i
    print(result-arr[0],result-arr[4])

def birthdayCakeCandles(candles):
    # Write your code here
    size = len(candles)
    cont = 0
    aux = 0
    for i in candles:
        if i > aux:
            cont = 1
            aux = i
        elif i == aux:
            cont += 1
    return cont

def timeConversion(s):
    if "PM" in s:
        hour = s[0:2]
        if hour != "12":
            s = s[2:]
            hour = int(hour)+12
            s = str(hour)+":"+s[1:]
        s = s[:-2]
    else:

        if s[0:2] == "12":
            s = s[2:]
            s = "00"+":"+s[1:]
        s = s[:-2]
    return s

def hourglassSum(arr):

    lst = [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]
           ]

    print("----------------------------------------------------")


    for x in range(0,len(arr),1):
        for y in range(0,len(lst[0]),1):
            lst[x][y] = arr[x][0+y] + arr[x][1+y] + arr[x][2+y]

    for x in range(2, len(arr), 1):
        for y in range(0, len(lst[0]), 1):
            lst[x-2][y ] = lst[x-2][y ] + lst[x][y]
    lst.pop()
    #lst.pop()

    for x in range(1,len(arr),1):

        for y in range(1,len(arr[0])-1,1):
            lst[x-1][y-1] = lst[x-1][y-1] + arr[x][y]

    lst.pop()
    cont = 0
    aux = lst[0][0]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] > aux:
                aux = lst[i][j]
            cont += 1
    return aux

def printList(lst):
    print("----------------------------------------------------")
    for x in lst:
        print(x)
    print("----------------------------------------------------")

"""25
0 6 -7 1 6 3
-8 2 8 3 -2 7
-3 3 -6 -3 0 -6
5 0 5 -1 -5 2
6 2 8 1 3 0
8 5 0 4 -7 4
 """
# 6-7+2-3+3-6
print(hourglassSum([
    [0, 6, -7, 1, 6, 3],
    [-8, 2, 8, 3, -2, 7],
    [-3, 3, -6, -3, 0, -6],
    [5, 0, 5, -1, -5, 2],
    [6, 2, 8, 1, 3, 0],
    [8, 5 ,0 ,4 ,-7, 4]
]))

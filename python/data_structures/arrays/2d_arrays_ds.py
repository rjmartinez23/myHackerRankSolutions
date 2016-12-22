#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
  
max_value = -100
for row_num in range(0, len(arr)-2):
  for column_num in range(0,len(arr)-2):
    sum = 0
    sum += arr[row_num][column_num] + arr[row_num][column_num+1] + arr[row_num][column_num+2]
    sum += arr[row_num+1][column_num+1]
    sum += arr[row_num+2][column_num] + arr[row_num+2][column_num+1] + arr[row_num+2][column_num+2]
    if sum >= max_value:
      max_value = sum

print(max_value)

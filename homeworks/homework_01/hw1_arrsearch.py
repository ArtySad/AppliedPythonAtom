#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):    
    i = 0
    j = len(input_list)-1
    while i !=j :
        if input_list[i] + input_list[j] == n:
            return i, j
        elif input_list[i] + input_list[j] < n:
           i = i+1
        elif input_list[i] + input_list[j] > n:
           j = j-1
    return

# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/24 20:18

def is_sorted(arr):
    if len(arr) <= 1:
        return True
    else:
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                return False
        return True
    
def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

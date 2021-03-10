# -*- coding: utf-8 -*-
# @Time : 2020/4/25 22:02

"""
参考：
https://zh.wikipedia.org/wiki/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F
https://www.geeksforgeeks.org/quick-sort/
"""

def partition(arr, low, high):
    i = (low - 1)  # smaller元素 pivot
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi -1)
        quickSort(arr, pi + 1, high)

if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    print('原数组：', arr)
    n = len(arr)
    quickSort(arr, 0, n - 1)
    print('排序后：', arr)
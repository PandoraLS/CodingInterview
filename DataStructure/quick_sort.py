def quick_sort(arr):
    if not arr or len(arr) == 1:
        return arr

    pivot = arr[0]
    left = [arr[i] for i in range(1, len(arr)) if arr[i] < pivot]
    right = [arr[i] for i in range(1, len(arr)) if arr[i] >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
    arr = [2, 3, 4, 2, 1, 3, 6, 9]
    print(quick_sort(arr))
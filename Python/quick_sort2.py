def quicksort(arr):
    if len(arr) <= 1:
        return arr
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return [arr[1], arr[0]]
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)


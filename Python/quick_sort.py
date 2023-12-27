def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
 
 
def qs(arr, low, high):
    if low < high:
        pivotidx = partition(arr, low, high)
        qs(arr, low, pivotidx - 1)
        qs(arr, pivotidx + 1, high)

def quicksort(arr):
    qs(arr, 0, len(arr)-1)


data = [2,5,3,1,6,5,4]
print(data)
quicksort(data)
print(data)

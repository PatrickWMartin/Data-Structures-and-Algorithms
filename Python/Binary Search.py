def binary_search(target, search_arr):
    left = 0
    right = len(search_arr)

    while left < right:
        mid = (left + right) // 2
        
        if mid > target:
            right = mid - 1
        elif mid < target:
            left = mid + 1
        else:
            return mid
        
    return None

    
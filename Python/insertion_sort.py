def insertion_sort(to_sort):
    n = len(to_sort)
    i = 1
    while i < n:
        j = i - 1
        current = to_sort[i]
        print(current)
        while j >= 0 and to_sort[j] > current:
            to_sort[j+1] = to_sort[j]
            j-=1
        to_sort[j+1] = current
        i+=1

    return to_sort
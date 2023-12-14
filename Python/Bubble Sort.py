def bubble_sort(to_sort):
    for idx,_ in enumerate(to_sort):
        for i,_ in enumerate(to_sort[:len(to_sort)-1-idx]):
            if to_sort[i] > to_sort[i+1]:
                to_sort[i], to_sort[i+1] = to_sort[i+1], to_sort[i]

    return to_sort

print(bubble_sort([3,7,4,1,2]))
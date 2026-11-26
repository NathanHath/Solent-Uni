def quicksort(list, start, end):
    if start < end:
        index = hoare_partition(list, start, end)
        quicksort(list, start, index-1)
        quicksort(list, index+1, end)



def hoare_partition(list, start, end):
    pivot = list[(start + end) // 2]
    i = start
    j = end
    while True:
        while list[i] < pivot:
            i += 1

        while list[j] > pivot:
            j -= 1

        if i >= j:
            return j

        list[i], list[j] = list[j], list[i]


list = [14, 28, 4, 57, 41, 33, 62, 92, 81, 76, -1,]
quicksort(list, 0, len(list)-1)
print(list)




import math
def binary_search(list, search_value):
    start=0
    end=len(list)-1


    while start <= end:
        mid = math.floor((start + end) / 2) # 49 (0-99)
        if list[mid] == search_value:
            return mid
        elif list[mid] < search_value: # start becomes 50, end is still 99, midpoint next time will be 74
            start = mid + 1
        else: # end becomes 48, start is still 0, midpoint next time will be 24
            end = mid - 1

    return -1 #can't be found
list = [i*i for i in range(100)]
print (binary_search(list))





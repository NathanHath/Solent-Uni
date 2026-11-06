import sys
numbers = [7, 4, 5, 9, 8, 2, 1]
def selection_sort(numbers):
    for i in range(len(numbers)-1):
        lowest_number_so_far = sys.maxsize
        for j in range(i, len(numbers)):



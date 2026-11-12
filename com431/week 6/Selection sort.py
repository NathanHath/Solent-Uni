import sys
numbers = [7, 4, 5, 9, 8, 2, 1]
def selection_sort(numbers):
    for i in range(len(numbers)-1):
        lowest_index = i
        for j in range(i+1, len(numbers)):
            if numbers[lowest_index] > numbers[j]:
                lowest_index = j

        numbers[lowest_index], numbers[i] = numbers[i], numbers[lowest_index]

selection_sort(numbers)
print(numbers)









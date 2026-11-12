numbers = [17, 54, 28, 83, 62]
def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        current_value = numbers[i]
        j = i - 1
        while current_value < numbers[j] and j>=0:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j+1] = current_value

insertion_sort(numbers)
print(numbers)






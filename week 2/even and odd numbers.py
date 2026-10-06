first_number = int(input("Enter a number: "))
second_number = int(input("Enter another number: "))
third_number = int(input("Enter another number: "))

even_numbers = 0
odd_numbers = 0

if first_number % 2 == 0:
    even_numbers += 1
else:
    odd_numbers += 1

if second_number % 2 == 0:
    even_numbers += 1
else:
    odd_numbers += 1

if third_number % 2 == 0:
    even_numbers += 1
else:
    odd_numbers += 1

print (f"there are {even_numbers} even numbers and {odd_numbers} odd numbers")

amount = int(input("How many numbers should I sum up?"))
count = 0
num_count = 1
while num_count <= amount:
    number = int(input(f"Please enter number {num_count} of {amount} "))
    num_count += 1
    count += number


print (count)
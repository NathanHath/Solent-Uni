steps = int(input("how may steps are you away from your goal? "))
count = steps
for _ in range(steps):
    print (f"{count} steps remaining")
    count -= 1
phrase = input("enter a sequence of characters consisting of dashes and two markers")
marker = input("enter marker character")

marker1 = -1
marker2 = -1
for count in range(len(phrase)):
    letter = phrase[count]
    if letter == marker and marker1 == -1:
        marker1 = count
    elif letter == marker and marker2 == -1:
        marker2 = count

distence = marker2 - marker1
print(f"The distance between the markers is {distence - 1}")


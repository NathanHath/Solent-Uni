phrase = input("Enter a phrase: ")
for count in range(len(phrase)-1, -1, -1):
    print(phrase[count], end=" ")
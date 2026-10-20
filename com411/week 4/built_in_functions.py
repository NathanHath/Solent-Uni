print ("Program stated!")
character = input("Enter a character: ")
if len(character) == 1:
    ASCII = ord(character)
    print (f"The ASCII code for {character} is {ASCII}.")
else:
    print ("Error")

print ("Program ended")
adventure_type = input("what is the type of adventure? ")
if adventure_type == "scary" or adventure_type == "short":
    print("entering the dark forst!")
elif adventure_type == "safe" or adventure_type == "long":
    print ("taking the unsafe route!")
else:
    print ("Not sure which route to take")

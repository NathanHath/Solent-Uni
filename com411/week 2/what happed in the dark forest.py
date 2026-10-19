hear = "y"
see = "x"
while hear != "grrr" and see != "two red eyes":
    hear = input("what did you hear? \n")
    see = input("what did you see? \n")

    if hear == "grrr" and see == "two red eyes":
        print ("There is a scary creature. I should get out of here!")
    else:
        print ("I am a little scared but I will continue")
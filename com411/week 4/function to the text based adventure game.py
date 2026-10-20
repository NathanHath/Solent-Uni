def identify():
    see = input("what do you see?\n")
    if see == "a large boulder":
        return "it's time to run"
    else:
        return "we will be fine."


print(identify())
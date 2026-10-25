def menu():
    while True:
        print ("""
        1) Display in a Box – display the word in an ASCII art box
        2) Display Lower-case – display the word in lower-case e.g. hello
        3) Display Upper-case – display the word in upper-case e.g. HELLO
        4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH
        5) Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case""")
        user_input = int(input("\n"))
        word = input("what is the word you are maliperuating?\n")
        match user_input:
            case 1:
                print(one(word))
            case 2:
                print(two(word))
            case 3:
                print(three(word))
            case 4:
                print(four(word))
            case 5:
                print(five(word))

def one(word):
    return (f"""
    +------------------------+

    |                        |
    |        {word}          |
    |                        |
    +------------------------+""")

def two(word):
    return word.lower()

def three(word):
    return word.upper()

def four(word):
    return word[::-1]

def five(word):
    amount = int(input("how many times would you like to display the word?\n"))
    return ("".join(char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(word))) * amount

menu()



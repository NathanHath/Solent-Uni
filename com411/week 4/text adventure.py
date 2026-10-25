def display_ladder(steps):
    print (""" 
    |===|
    |   |""" * steps)
def create_ladder():
    steps = int(input("Enter number of steps: "))
    return steps

display_ladder(create_ladder())
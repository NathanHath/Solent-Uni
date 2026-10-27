def directions():
    steps = [ "Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps

def menu_and_input():
    print ("Enter your choice:")
    step = directions()
    for i in range(len(step)):
        print (f"{i}: {step[i]}")
    return int(input())


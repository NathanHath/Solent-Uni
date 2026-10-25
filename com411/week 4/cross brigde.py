def cross_brigde(step_distance):
    for i in range(step_distance):
        print ("Crossed step")
    if step_distance > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going")


cross_brigde(10)



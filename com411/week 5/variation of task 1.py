def movements():
    paths =["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return paths

def run_task2():
    print("moving...")
    steps = movements()
    for i in range(0, len(steps), 2):
        print (f"move {steps[i]} for {steps[i+1]}")

run_task2()



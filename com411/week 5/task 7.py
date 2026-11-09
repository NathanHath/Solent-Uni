def step():
    likelihood = [("step 1", 50),("step 2", 38),("step 3", 27),("step 4", 99),("step 5", 4)]
    return likelihood

def run_task3():
    steps = step()
    goodsteps = []
    badsteps = []
    for current_step in steps:
        stage, number = current_step
        if number >= 50:
            goodsteps.append(current_step)
        else:
            badsteps.append(current_step)
    return goodsteps, badsteps

num_goodsteps, num_badsteps = run_task3()
print(f"good staps {len(num_goodsteps)}, bad staps {len(num_badsteps)}")

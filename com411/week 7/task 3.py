def observed_items():
    observations = []
    for i in range(5):
        observations.append(input(":"))
    return observations

def remove_observations(observations):
    user = input ("do you want to remove a observations? ")
    if user == "yes":
        print (observations)
        user = input ("what do you want to remove? ")
        observations.remove(user)

    return observations

def run_task3():
    observations = observed_items()
    print (sorted(set(remove_observations(observations))))
run_task3()
def observed_items():
    observations = []
    for i in range (1, 8):
        item = input((f"what is the {i} number item you want to add to the list, make sure to add duplicate numbers"))
        observations.append(item)
    return observations

def run_task2():
    observations = observed_items()

    observations_set = set()
    for observation in observations:
        data = (observation, observations.count(observation))
        observations_set.add(data)
    # display set

    for data in observations_set:
        print(f"{data[0]} observed {data[1]} times.")

run_task2()


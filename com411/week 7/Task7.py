import json

def read(filename):
    with open(filename) as f:
        content = json.load(f)
        locations = content["location"]
        population_size = content["population"]
        print (f"Place Name:{locations}")
        print(f"Population Size: {population_size}")
        for bot in content["bots"]:
            name = bot["name"]
            stats = bot["stats"]
            print(f"{name} has the following stats: {stats}")

read("futurama.json")

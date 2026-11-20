def pattern():
    sequences = { "Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return sequences

def display_keys(data):
    for key in data:
        print(key)

def display_values(data):
    for value in data.values():
        print(value)

def display_items(data):
    for key, value in data.items():
        print(key, value)

def run():
    print(pattern())
    data = pattern()
    display_values(data)
    display_keys(data)
    display_items(data)

run()



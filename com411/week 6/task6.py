import csv

def extract(filename):
    print("Extracting data...")
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        names = ""
        for values in reader:
            names += f"{values[1]}\n"
    print("Done!")
    print(f"The extracted items are:\n{names}")


def run_task2():
    extract("clothing.csv")

run_task2()
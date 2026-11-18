import csv

def read_csv(filename):
    with open(filename) as f:
        reader = csv.reader(f)

        headings = next(reader)
        print(f"Headings:\n{headings}")

        print("Values:")
        for value in reader:
            print(value)

def run_task5():
    read_csv("clothing.csv")

run_task5()
def search(file_name):
    print ("searching...")
    with open(file_name) as file:
        for line in file:
            print (f"looked in {line.strip()}")

    print ("Done")
def run_task3():
    search("liberary")

run_task3()



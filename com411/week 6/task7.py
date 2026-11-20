import csv

def export(export_file, num):
       for i in range(num):
        print ("Exporting...")
        id = int(input("What is the item id you would like to export?\n:"))
        name = input("What is the name of the item you would like to export?\n:")
        clour = input("What is the item colour you would like to export?\n:")

        with open(export_file, "a") as f:
            f.write(f"{id},{name},{clour}\n")

        print("Exported successfully!")



def task7():
    export("exported_items.csv", 1)

task7()



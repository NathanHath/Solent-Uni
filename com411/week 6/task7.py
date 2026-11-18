import csv

def export(current_file, export_file):
    with open(current_file) as f:
        reader = csv.DictReader(csvfile)

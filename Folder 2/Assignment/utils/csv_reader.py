import csv
import os

def read_data_from_csv(filename):
    datalist = []
    filepath = os.path.join(os.path.dirname(__file__), '..', 'testdata', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader) # skip header
        for row in reader:
            datalist.append(tuple(row))
    return datalist

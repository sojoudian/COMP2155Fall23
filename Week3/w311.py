#working woth CSV files in Python

# CSVfile = open("file.csv", "r")
# a=CSVfile.read()
# print(a)

import csv
with open("file.csv", "r+") as f:
    data = csv.reader(f)
    for row in data:
        print(row, end="\n")
    f.close()
import csv

with open('some.csv', newline='') as csvfile:
    rdr = csv.reader(csvfile, delimiter = ',')
    for row in rdr:
        print(', '.join(row)) #  collat rows
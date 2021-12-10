import csv
import os

files = os.listdir('./reports')
for file_name in files:
    print(file_name)
    if (file_name[-3:] != "csv"): continue
    with open('./reports/{a}'.format(a=file_name), newline='') as csvfile:
        rdr = csv.reader(csvfile, delimiter = ',')
        for row in rdr:
            print(','.join(row)) #  collat rows

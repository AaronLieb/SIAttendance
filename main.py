import csv
from tkinter import filedialog as fd
import os

times = {}

csv_folder_dir = './reports'
#csv_folder_dir = fd.askdirectory()
files = os.listdir(csv_folder_dir)
for file_name in files:
    if (file_name[-3:] != "csv"): continue
    with open(csv_folder_dir + '/' + file_name, newline='') as csvfile:
        rdr = csv.reader(csvfile, delimiter = ',')
        next(rdr)
        for row in rdr:
            print(','.join(row)) #  collat rows
            email = str(row[1])
            if email in times:
                times[email][1] += int(row[2])
            else:
                times[email] = (str(row[0]), int(row[2]))
    for p1 in times:
        for p2 in times:
            if p1 is p2:
                continue
            if (times[p1][0] == times[p2][0]):
                merge = str(input('Duplicate names found, are these the same person? (Y/N): \n {a} \n {b} \n {c}\n'.format(a=times[p1][0],b=p1,c=p2)))
                if (merge.lower() == 'y'):
                    times[p1][1] += times[p2][1]
                    times.pop(p2)


        



                

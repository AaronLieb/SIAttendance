import csv
from tkinter import filedialog as fd
import os


times = dict[str, tuple[str,int]]

#csv_folder_dir = fd.askdirectory()
#files = os.listdir(csv_folder_dir)
files = os.listdir('./reports')
for file_name in files:
    print(file_name)
    if (file_name[-3:] != "csv"): continue
    with open(csv_folder_dir + '/' + file_name, newline='') as csvfile:
        rdr = csv.reader(csvfile, delimiter = ',')
        rdr.next()
        for row in rdr:
            print(','.join(row)) #  collat rows
            if row[1] in times:
                times[row[1]][1] += int(row[2])
            else:
                times[row[1]][0] = row[0]
                times[row[1]][1] = row[2]



                

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
    """for(p1 in times):
        for (p2 in times):
        """



                

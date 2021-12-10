import csv
from tkinter import filedialog as fd
csv_folder_dir = fd.askdirectory()
import os

files = os.listdir(csv_folder_dir)
for file_name in files:
    print(file_name)
    if (file_name[-3:] != "csv"): continue
    with open(csv_folder_dir + '/' + file_name, newline='') as csvfile:
        rdr = csv.reader(csvfile, delimiter = ',')
        for row in rdr:
            print(','.join(row)) #  collat rows

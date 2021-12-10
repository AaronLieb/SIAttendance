import csv
from tkinter import filedialog as fd

csv_folder_dir = fd.askdirectory()

with open('./inp/test.csv', newline='') as csvfile:
    rdr = csv.reader(csvfile, delimiter = ',')
    for row in rdr:
        print(', '.join(row)) #  collat rows
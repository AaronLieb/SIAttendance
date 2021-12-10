import csv
from tkinter import filedialog as fd
import os

sessions_attended = {}

csv_folder_dir = './reports'
#csv_folder_dir = fd.askdirectory()
files = os.listdir(csv_folder_dir)

for file_name in files:
    if (file_name[-3:] != "csv"): continue
    with open(csv_folder_dir + '/' + file_name, newline='') as csvfile:
        rdr = csv.reader(csvfile, delimiter = ',')
        next(rdr)
        for row in rdr:
            email = str(row[1])
            if int(row[2]) < 10:
                continue
            if email in sessions_attended:
                sessions_attended[email][1] += 1
            else:
                sessions_attended[email] = (str(row[0]),1 ) 
    for p1 in sessions_attended:
        for p2 in sessions_attended:
            if p1 is p2:
                continue
            if (sessions_attended[p1][0] == sessions_attended[p2][0]):
                merge = str(input('Duplicate names found, are these the same person? (Y/N): \n {a} \n {b} \n {c}\n'.format(a=sessions_attended[p1][0],b=p1,c=p2)))
                if (merge.lower() == 'y'):
                    sessions_attended[p1][1] += sessions_attended[p2][1]
                    sessions_attended.pop(p2)


        



                

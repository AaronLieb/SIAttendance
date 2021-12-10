import csv
from tkinter import filedialog as fd
import os

times = {}

default_prof = input()

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

def dict_to_csv(write_file, dict_data):
    with open(write_file, 'w') as towrite:
        writer = csv.writer(towrite)
        for item in dict_data.items():
            email = item[0]
            name, minutes = item[1] # change min to sesh
            name_list = name.split(' ')
            name_list.reverse()
            formatted_name = ', '.join(name_list)

            writer.writerow((formatted_name, default_prof, minutes))
#        writer.writerows(dict_data.items())

if __name__ == '__main__':
    dict_to_csv('./output.csv', times)
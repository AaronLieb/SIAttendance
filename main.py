import csv
from tkinter import filedialog as fd
import os
from collections import defaultdict


MIN_MINUTES = 10
sessions_attended = defaultdict(lambda : 0)

default_prof = input('Enter the name of the default professor: ')
default_section = input('Enter the name of the default section: ')

#csv_folder_dir = './reports'
csv_folder_dir = fd.askdirectory()
files = os.listdir(csv_folder_dir)

for file_name in files:
    if (file_name[-3:] != "csv"): continue
    with open(csv_folder_dir + '/' + file_name, newline='') as csvfile:
        rdr = csv.reader(csvfile, delimiter = ',')
        headers = next(rdr)
        minute_column = None
        attended = []
        for header in headers:
            if 'Duration' in header:
                minute_column = headers.index(header)
        for row in rdr:
            name = str(row[0])
            if name in attended or int(row[minute_column]) < MIN_MINUTES:
                continue
            sessions_attended[name] += 1
            attended.append(name)

def dict_to_csv(write_file, dict_data):
    with open(write_file, 'w') as towrite:
        writer = csv.writer(towrite, lineterminator='\n')
        items = sorted(dict_data.items(), key=lambda kv: kv[1], reverse=True)
        for item in items:
            name = item[0]
            sessions = item[1] 
            name_list = name.split(' ')
            name_list.reverse()
            formatted_name = ', '.join(name_list)

            if sessions <= 0:
                continue
            writer.writerow((formatted_name, default_prof, default_section, sessions))

if __name__ == '__main__':
    try:
        dict_to_csv('./output.csv', sessions_attended)
    except Exception as e:
        print(e)
    else:
        print("output.csv file has been generated\n Love, Justin & Aaron")

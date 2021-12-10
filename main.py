import csv
from tkinter import filedialog as fd
import os

sessions_attended = {}

default_prof = input('Enter the name of the professor: ')

#csv_folder_dir = './reports'
csv_folder_dir = fd.askdirectory()
files = os.listdir(csv_folder_dir)

for file_name in files:
    if (file_name[-3:] != "csv"): continue
    with open(csv_folder_dir + '/' + file_name, newline='') as csvfile:
        rdr = csv.reader(csvfile, delimiter = ',')
        headers = next(rdr)
        minute_column = None
        for header in headers:
            if 'Duration' in header:
                minute_column = headers.index(header)
        for row in rdr:
            email = str(row[1])
            if int(row[minute_column]) < 10:
                continue
            if email in sessions_attended:
                sessions_attended[email][1] += 1
            else:
                sessions_attended[email] = [str(row[0]), 1] 
    for p1 in sessions_attended:
        for p2 in sessions_attended:
            if p1 is p2:
                continue
            if (sessions_attended[p1][0] == sessions_attended[p2][0]):
                merge = str(input('Duplicate names found, are these the same person? (Y/N): \n {a} \n {b} \n {c}\n'.format(a=sessions_attended[p1][0],b=p1,c=p2)))
                if (merge.lower() == 'y'):
                    sessions_attended[p1][1] += sessions_attended[p2][1]
                    sessions_attended[p2][1] = 0
                    sessions_attended[p2][0] = ''

def custom_key(item):
    return item[1][1]

def dict_to_csv(write_file, dict_data):
    with open(write_file, 'w') as towrite:
        writer = csv.writer(towrite)
        items = list(sorted(dict_data.items(), key = lambda x : x[1][1], reverse=True))
        for item in items:
            email = item[0]
            name, sessions = item[1] 
            name_list = name.split(' ')
            name_list.reverse()
            formatted_name = ', '.join(name_list)

            if sessions <= 0:
                continue
            writer.writerow((formatted_name, default_prof, '', sessions))

if __name__ == '__main__':
    try:
        dict_to_csv('./output.csv', sessions_attended)
    except Exception as e:
        print(e)
    else:
        print("output.csv file has been generated\n Love, Justin & Aaron")

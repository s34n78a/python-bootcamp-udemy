import csv
import os

def open_path(file_name):
    csv_path = os.path.join(os.getcwd(), "pdf & csv", file_name)
    try:
        data = open(csv_path, encoding='utf-8')
        return data
    except IOError:
        print("Unable to open CSV file.")

data = open(os.path.join(os.getcwd(), "pdf & csv", 'example.csv'))
data_list = data.read().splitlines()
csv_data = csv.reader(data_list)
data_lines = list(csv_data)
data.close()
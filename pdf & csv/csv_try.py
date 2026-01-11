import csv
import os

def path_join_cwd(file_name):
    csv_path = os.path.join(os.getcwd(), "pdf & csv", file_name)
    return csv_path

data = open(path_join_cwd('example.csv'),encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)
#print(data_lines)

for line in data_lines[:10]:
    print(line)

data.close()
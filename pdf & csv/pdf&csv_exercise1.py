import os
import csv

def path_join_cwd(file_name):
    file_path = os.path.join(os.getcwd(), "pdf & csv", file_name)
    return file_path

data = open(path_join_cwd('find_the_link.csv'),encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)
#print(len(data_lines))
i = 0
link = ''
for line in data_lines:
    link += line[i]
    i+=1

print(link)

data.close()
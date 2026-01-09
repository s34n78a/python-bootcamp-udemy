import os
import re

cwd = os.getcwd()
#print(cwd)

path_soal = cwd + '/soal_unzip/extracted_content'
#print(path_soal)

folder_list = os.listdir(path_soal)
#print(folder_list)

filtered_folder_list = [folder_list[x] for x in range(len(folder_list)) if '.' not in folder_list[x]]
#print(filtered_folder_list)

phone = ''
pattern = r'\d{3}-\d{3}-\d{4}'

for folder_name in filtered_folder_list:
    folder_path = path_soal+'/'+folder_name
    #print(folder_path)

    files_list = os.listdir(folder_path)
    #print(files_list)

    for file in files_list:
        file_path = folder_path + '/' + file
        #print(file_path)

        with open(file_path, 'r') as f:
            content = f.read()
            #print(content)

            phone = re.search(pattern, content)
        
        if phone != '' and phone is not None:
            print(phone.group())
            #print(file_path)
            #print(content)
            break
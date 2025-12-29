import shutil
import os
import zipfile

# cwd = os.getcwd()
# print(cwd)
# filepath = cwd + '/unzip_me_for_instructions.zip'
# print(filepath)

# shutil.make_archive('testing_zip', 'zip', cwd)
# shutil.unpack_archive('testing_zip', cwd+'/test', 'zip')
# shutil.unpack_archive('unzip_me_for_instructions', cwd,'zip')

soal_zip_obj = zipfile.ZipFile('unzip_me_for_instructions.zip','r')
soal_zip_obj.extractall('soal_unzip')
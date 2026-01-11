import os
import pypdf
import re

def path_join_cwd(file_name):
    file_path = os.path.join(os.getcwd(), "pdf & csv", file_name)
    return file_path

document = open(path_join_cwd('Find_the_Phone_Number.pdf'), 'rb')
doc_reader = pypdf.PdfReader(document)

max_page = doc_reader.get_num_pages()
page_num = 0
phone_pattern = r'\d{3}.\d{3}.\d{4}'

while page_num < max_page:
    text = doc_reader.get_page(page_num).extract_text()
    phone = re.search(phone_pattern, text)
    if phone:
        print(f'Phone number found on page {page_num + 1}: {phone.group()}')
        break
    page_num += 1

document.close()
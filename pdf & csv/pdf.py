import pypdf
import os

def path_from_root(*path_segments):
    return os.path.join(os.path.dirname(__file__), *path_segments)

f = open(path_from_root('Working_Business_Proposal.pdf'), 'rb')
pdf_reader = pypdf.PdfReader(f)
print(pdf_reader.get_num_pages())

page_one = pdf_reader.get_page(0)
#print(page_one.extract_text())
print(type(page_one))

pdf_writer = pypdf.PdfWriter()
pdf_writer.add_page(page_one)
pdf_output = open(path_from_root('First_Page_Proposal.pdf'), 'wb')
pdf_writer.write(pdf_output)

f.close()
pdf_output.close()
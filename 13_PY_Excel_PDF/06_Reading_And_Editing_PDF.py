# Reading and editing pdf files in python 

# There's a module call PyPDF2 that helps us work 
# with PDF files much easier 
import os 
import PyPDF2

os.chdir('..\\13_PY_Excel_PDF\\')

# NOTE When working with pdf, it needs to be 'rb' for 
# Read Binary, PDF's are binary files 

pdfFile = open('Luke-Sorrenti-Resume.pdf', 'rb')
reader = PyPDF2.PdfReader(pdfFile)
print(len(reader.pages))
# 2

page = reader.pages[0]

print(page.extract_text())
# Hi there! I'm Luke, I've been learning and creating.... 

# To get all the text from all the pages, use 
# a loop:

for pageNum in range(len(reader.pages)):
    page = reader.pages[pageNum]
    print(page.extract_text())
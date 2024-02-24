# You can extract strings from a docx file 

import docx

def getText(filename):
    # this function will return a string value of 
    # all the text of a word doc
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    print('\n'.join(fullText))
    return '\n'.join(fullText)

getText('./demo.docx')
# Document Title
# A plain paragraph having some bold and some italic.
# Heading, level 1
# Intense quote
# first item in unordered list
# first item in ordered list
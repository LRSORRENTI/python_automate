# Recap

- The PyPDF2 module can read and write PDF's

- Opening a PDF is done by calling open() and passing the file object to PfFFileReader()

- A Page object can be obtained from the pdf object with the getPage() method

- The text from a Page object is obtained with the extractText() method, which can be imperfect

- New PDF's can be made with PdfFileWriter()

- New pages can be appended to the writer object using addPage()

- Call the write() method to save it's changes

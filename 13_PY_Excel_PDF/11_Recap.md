# Recap

- Python-Docx can read and write to .docx word files

- Open a Word file with the docx.Document() method

- Access one of the Paragraph objects from the paragraphs member variable, which is a list of Paragraph objects

- Paragraphs are composed of 'runs', the runs member variable of a Paragraph object contains a list of Run objects

- Run objects also have text member variables

- Run objects can have a bold, italic, and underline member variables, that can be activated with True, or False

- Paragraph and run objects have a style member variable that can be set to one of Word's built in styles

- Word files can be created by using:

```
d = docx.Document()


d.add_paragraph("Hello from Python! This paragraph\
                was created with .add_paragraph method")

d.add_paragraph('Another paragraph')

p = d.paragraphs[0]
p.add_run('This is a new run')
p.runs[1].bold = True

d.save('.\\brand_new_docx_file.docx')
```

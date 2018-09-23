import docx

def getText(filepath):
    doc = docx.Document(filepath)
    fulltext = []
    context = doc.paragraphs
    for para in context:
        fulltext.append(para.text)
    return fulltext

data = getText("tangshan.docx")
for line in data:
    print(line)
    pass
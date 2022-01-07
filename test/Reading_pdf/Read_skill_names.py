import PyPDF2


pdfFileObj = open('ZewCthulhu_7ed_Karta-Badacza_ArtDeco.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)

pageObj = pdfReader.getPage(1)

file = open("extraction.txt", "w")
file.write(str(pageObj.extractText().encode('utf-8')))
file.close()

pdfFileObj.close()

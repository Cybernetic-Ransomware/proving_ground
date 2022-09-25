import pikepdf
from PyPDF2 import PdfFileReader, PdfFileWriter


pages_WH, pages_CN = [192, 202], [296, 308]
pages = [list(range(book[0], book[1])) for book in (pages_WH, pages_CN)]
sources = ['Warhammer_RPG_4_ed.pdf', 'Conan-Przygody_w_erze_niewysnionej.pdf']


for file in sources:
    pdf = pikepdf.open(file)
    pdf.save(file[:4] + '_encrypted' + '.pdf')


for pages, book in zip(pages, sources):
    with open(book[:4] + '_encrypted' + '.pdf', 'rb') as pdf:
        reader = PdfFileReader(pdf)
        writer = PdfFileWriter()
        # rest_writer = PdfFileWriter()

        for page in range(len(reader.pages)):
            if page in pages:
                writer.addPage(reader.getPage(page))
            # else:
            #     rest_writer.addPage(reader.getPage(page))

        with open(book[:4] + '_splited' + '.pdf', 'wb') as splited:
            writer.write(splited)

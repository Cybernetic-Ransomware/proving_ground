from PyPDF2 import PdfFileMerger


file_list = ["Warh_splited.pdf", "Cona_splited.pdf"]
merger = PdfFileMerger()


for pdf in file_list:
    merger.append(pdf)

merger.write('merged_files.pdf')
merger.close()

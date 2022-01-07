import tabula


df = tabula.read_pdf("ZewCthulhu_7ed_Karta-Badacza_ArtDeco.pdf", pages='all')[0]
tabula.convert_into("IPLmatch.pdf", "iplmatch.csv", output_format="csv", pages='all')

print(df)

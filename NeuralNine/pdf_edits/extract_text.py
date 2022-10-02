import re

from pdfminer.high_level import extract_pages, extract_text


# for page_layoyut in extract_pages('WFRP_4e_Shrines_of_Sigmar.pdf'):
#     for element in page_layoyut:
#         print(element)


text = extract_text('WFRP_4e_Shrines_of_Sigmar.pdf').replace('\n', ' ')
text = re.sub(' +', ' ', text)


# pattern = re.compile(r'[a-zA-Z]+,{1}\s{1}')
# matches = pattern.findall(text)
# names = [n[:-2] for n in matches]


pattern = re.compile(r'.{1}\s{1}[A-Za-z," ]+Sigmar[A-Za-z," ]+.{1}\s{1}')
matches = pattern.findall(text)

for line in matches:
    if line[2].isupper() and line[-2] == '.':
        print(line[2:-1])
        print('-' * 10)

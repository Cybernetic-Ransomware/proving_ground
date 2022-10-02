import fitz
import PIL.Image
import io
import os


try:
    os.mkdir('extracted')
except FileExistsError:
    print("Directory 'extracted' already exists")


pdf = fitz.open('WFRP_4e_Shrines_of_Sigmar.pdf')
counter = 1


for i in range(len(pdf)):
    page = pdf[i]
    images = page.get_images()

    for image in images:
        base_img = pdf.extract_image(image[0])
        if base_img['height'] >100 and base_img['width'] > 100:
            img_data = base_img['image']
            img = PIL.Image.open(io.BytesIO(img_data))
            extension = base_img['ext']
            img.save(open(f'./extracted/image{counter}.{extension}', 'wb'))
            counter += 1

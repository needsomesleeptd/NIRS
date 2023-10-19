
import fitz
import io
import os
from PIL import Image

path_to_pdf = "./pdfs/main.pdf"

output_format = "png"
output_dir = "./images/"
# open the file
pdf_file = fitz.open(path_to_pdf)

for page_index in range(len(pdf_file)):
    page = pdf_file[page_index]
    image_list = page.get_images(full=True)


    for image_index, img in enumerate(image_list, start=1):
        # Get the XREF of the image
        xref = img[0]
        d = pdf_file.extract_image(xref)
        print(d,image_index)
        #print(xref,image_index)





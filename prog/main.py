import fitz
import io
import os
from PIL import Image


def extract_images_from_pdf(pdf_path, output_folder, dpi=180): #make dpi lower if low
    pdf_document = fitz.open(pdf_path)

    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        image = page.get_pixmap(matrix=fitz.Matrix(dpi/72, dpi/72),alpha=False)
        pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
        pil_image.save(f"{output_folder}/page_{page_number + 1}.png", dpi=(dpi, dpi))


    pdf_document.close()


path_to_pdf = "./pdfs/main.pdf"

output_format = "png"
output_dir = "./data/"
# open the file
extract_images_from_pdf(path_to_pdf, output_dir)

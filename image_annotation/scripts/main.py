import fitz
import io
import os
from PIL import Image


def extract_images_from_pdf(pdf_path, output_folder, prefix, dpi=180):  # make dpi lower if low
    pdf_document = fitz.open(pdf_path)

    for page_number in range(pdf_document.page_count):
        if page_number != 0:
            page = pdf_document[page_number]
            image = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), alpha=False)
            pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
            pil_image.save(f"{output_folder}/{prefix}_{page_number + 1}.png", dpi=(dpi, dpi))

    pdf_document.close()


path_to_pdfs = "../reports/"
path_to_images = "../images/"
output_format = "png"

reports = os.listdir(path_to_pdfs)
for report in reports:
    output_dir = os.path.join(path_to_images, report.removesuffix('.pdf'))
    # print(report)
    os.makedirs(output_dir,exist_ok=True)
    extract_images_from_pdf(path_to_pdfs + report, output_dir,report)

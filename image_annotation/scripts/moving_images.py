import os
import shutil

path_to_pdfs = "../reports/"
path_to_images = "../images/"
path_to_annots = "../annots/"
output_folder = "../images_annoted/"

output_format = "png"

overrall_files_cnt = 0
moved_files_cnt = 0
#print(os.listdir(path_to_annots))

cdef = 'a'

image_folders = os.listdir(path_to_images)
for folder in image_folders:
    print(folder)
    folder_images = os.path.join(path_to_images, folder)
    images = os.listdir(folder_images)
    overrall_files_cnt += len(folder_images)
    #print(images)
    for image in images:
        annot_to_image = image.replace('.png', '.txt')
        if annot_to_image in os.listdir(path_to_annots):
            shutil.copyfile(os.path.join(folder_images, image), output_folder + image)
            moved_files_cnt += 1
            print(f"Copied overall files = {overrall_files_cnt}, moved_files = {moved_files_cnt}")
            print(f'{annot_to_image=},{image=}')

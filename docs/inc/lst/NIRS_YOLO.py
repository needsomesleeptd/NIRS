import os
import numpy as np
import pandas as pd
import shutil
import cv2
import random
import matplotlib.pyplot as plt
import copy

#!pip install ultralytics необходимо установить ultralitics



#!unzip /datasets/NIRS/annots.zip  необходимо распаковать датасет

#!unzip /datasets/NIRS/images_annoted.zip  необходимо распаковать датасет

import numpy as np
import cv2



path_images = '/content/images_annoted/'
path_annots = '/content/annots/'

img_name = 'ReportLab01.pdf_11'

annot_name = 'ReportLab01.pdf_11.png'

image = cv2.imread('/content/images_annoted/ReportLab01.pdf_11.png')
height = np.size(image, 0)
width = np.size(image, 1)
cv2.imshow(image)

def draw_bbs(image_name,ext = '.png'):
  print(path_images + image_name +ext)
  image = cv2.imread(path_images + image_name +ext)
  annots_file = path_annots + image_name + '.txt'
  lines = open(annots_file).readlines()
  print(image.shape)
  image_height = image.shape[0]
  image_width = image.shape[1]
  for line in lines:
    bbox_yolo_format = list(map(float,line.split()))[1:]
    print(bbox_yolo_format)
    x, y, width, height = int(bbox_yolo_format[0] * image_width), int(bbox_yolo_format[1] * image_height), int(bbox_yolo_format[2] * image_width), int(bbox_yolo_format[3] * image_height)
    color =(255, 0, 0)
    thickness = 2
    cv2.rectangle(image, (x - width // 2, y - height // 2), (x + width // 2, y + height // 2), color, thickness)
  cv2.imshow(image)


img_name = '/report-31.pdf_5'

draw_bbs(img_name)

from ultralytics import YOLO

model=YOLO('yolov8n.yaml').load('yolov8n.pt')

config = '''
train: '/content/images/train'
val: '/content/images/test'
# Classes
names:
  0: dog
  1: person
  2: cat
  3: tv
  4: car
  5: meatballs
  6: marinara sauce
  7: tomato soup
  8: chicken noodle soup
  9: french onion soup
  10: chicken breast
  11: ribs
  12: pulled pork
  13: hamburger
  14: cavity
  15: eq
  16: scheme
  17: table
  18: pic
  19: graph
  20: lit'''

config_name = "config.yaml"

with open(config_name,'w') as f:
  f.write(config)


val_size = 0.1
train_size = 0.9

os.rename('images_annoted','images')

os.rename('annots','labels')

path_images = '/content/images/'
path_annots = '/content/labels/'

labels = list(os.listdir('/content/labels'))
train_labels = labels[:int(len(labels) * train_size)]
val_labels = labels[int(len(labels) * train_size):]

images= list(os.listdir('/content/images'))
train_images = images[:int(len(images) * train_size)]
val_images = images[int(len(images) * train_size):]

os.makedirs('train')

os.makedirs('test')

for image in train_images:
  shutil.move(path_images + image,'train/')



shutil.move('train','images/')




for image in val_images:
  shutil.move(path_images + image,'test/')


shutil.move('test','images/')

os.makedirs('train')

os.makedirs('test')

for label in train_labels:
  shutil.move(path_annots + label,'train/')


shutil.move('train','labels/')

for label in val_labels:
  shutil.move(path_annots + label,'test/')

#!mv test labels/
shutil.move('test','labels/')


results=model.train(data=config_name, epochs=10, resume=True, iou=0.5, conf=0.001)



def show_model_perfomance(images):
  plt.figure(figsize=(60,60))

  for i in range(1,8,2):
      test_image=images[i]
      ax=plt.subplot(4,2,i)

      # Display actual image
      plt.imshow(cv2.imread(test_image))
      plt.xticks([])
      plt.yticks([])
      plt.title("Actual image", fontsize = 40)

      # Predict
      res = model(test_image)
      res_plotted = res[0].plot()
      ax=plt.subplot(4,2,i+1)

      # Display image with predictions
      plt.imshow(res_plotted)
      plt.title("Image with predictions", fontsize = 40)
      plt.xticks([])
      plt.yticks([])


val_img_path = '/content/images/test/'

val_images_paths = list(map(lambda x: val_img_path + x,val_images))


show_model_perfomance(val_images_paths)

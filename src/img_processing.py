import cv2
import os
import numpy as np
from operation import *

def list_files(directory):
  list_of_files = []
  for folder, direct, file in os.walk(directory):
    for f in file:
      list_of_files.append(os.path.join(folder, f))
  return list_of_files

def get_image(path):
  images = []
  for image in list_files(path):
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    if img is not None:
      images.append(img)
  return images

def resize_image(images, size):
  resized_images = []
  for image in images:
    resized_images.append(cv2.resize(image, size))
  return resized_images


#S = resize_image(get_image(".\dataset\pins_Adriana Lima"), (256, 256))
S = resize_image(get_image("./test/dataset/AA"), (256, 256))
printMatriks(S)
print(S)
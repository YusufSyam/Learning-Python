import cv2
from pyzbar.pyzbar import decode
import os

for img_dir in os.listdir('img'):
  img= cv2.imread(f'img/{img_dir}')
  
  print(f'Image: {img_dir}')
  for code in decode(img):
      print(f'Code Type: {code.type}')
      print(f'Code: {code.data.decode("utf-8")}')

  print()
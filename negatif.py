import imageio.v3 as img
import numpy as np

path = r"C:\Users\alifr\OneDrive\Documents\Meylinda Nuryani\PCD4MEYLINDA\Negatif.jpeg"

image = img.imread(path)

image_neg = 255 - image

img.imwrite("C:\\Users\\alifr\\OneDrive\\Documents\\Meylinda Nuryani\\PCD4MEYLINDA\\Negatif1.jpg",image_neg)

import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

path = path = r"C:\Users\alifr\OneDrive\Documents\Meylinda Nuryani\PCD4MEYLINDA\Negatif.jpeg"

image = img.imread(path)

image_neg = 255 - image

r_image = image[:,:,0]
r_neg = image_neg[:,:,0]

hist_r, bins_r = np.histogram(r_image.flatten(), bins=256, range =[0,256])
hist_rn, bins_rn = np.histogram(r_neg.flatten(), bins=256, range =[0,256])

plt.figure(figsize=(10,7))
plt.subplot(2,1,1)
plt.plot(hist_r, color="red", label="Histogram R Awal")

plt.subplot(2,1,2)

plt.plot(hist_rn, color="green", label="Histogram R negatif")


plt.show()
img.imwrite("C:\\Users\\alifr\\OneDrive\\Documents\\Meylinda Nuryani\\PCD4MEYLINDA\\Negatif1.jpg", image_net)
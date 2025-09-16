from PIL import Image
import numpy as np

img = np.array(Image.open('1.png'))
img_red = img.copy()
img_red[:, :, (1, 2)] = 0
img_green = img.copy()
img_green[:, :, (0, 2)] = 0
img_blue = img.copy()
img_blue[:, :, (0, 1)] = 0
img_ORGB = np.concatenate((img, img_red, img_green, img_blue), axis=1)
img_converted = Image.fromarray(img_ORGB)
img_converted.show()  ## Combine Image Contains all four images

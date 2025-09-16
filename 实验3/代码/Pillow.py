from PIL import Image,ImageEnhance
img_original = Image.open("1.png")
img_original.show("Original Image")
img = ImageEnhance.Contrast(img_original)
img.enhance(3.8).show("Image With More Contrast")

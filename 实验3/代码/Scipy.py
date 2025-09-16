import matplotlib
matplotlib.use('TkAgg')  # 在导入pyplot之前设置后端
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from PIL import Image

# 读取图像
image = Image.open('1.png')
image_array = np.array(image)

# 应用高斯模糊
sigma = 3
blurred_image = ndimage.gaussian_filter(image_array, sigma=sigma)

# 显示图像
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image_array)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(blurred_image)
plt.axis('off')

plt.tight_layout()
plt.show()

# 保存结果
blurred_pil = Image.fromarray(blurred_image)
blurred_pil.save('blurred_image.jpg')
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from skimage import io, color
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 读取图像
image = io.imread('1.png')  # 替换为你的图像路径
print(f"图像形状: {image.shape}")
print(f"图像数据类型: {image.dtype}")

# 如果图像有4个通道（RGBA），移除Alpha通道
if image.shape[2] == 4:
    image = image[:, :, :3]  # 只取前3个通道（RGB）
    print(f"处理后图像形状: {image.shape}")

# 转换为灰度图
gray_image = color.rgb2gray(image)

# 显示图像
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')  # 使用英文标题避免中文问题
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')  # 使用英文标题
plt.axis('off')

plt.tight_layout()
plt.show()

# 保存处理后的图像（可选）
from skimage import img_as_ubyte
io.imsave('gray_image.jpg', img_as_ubyte(gray_image))
print("灰度图像已保存为 gray_image.jpg")
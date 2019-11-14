import tesserocr
from PIL import Image

image = Image.open('code.jpg')
result = tesserocr.image_to_text(image)
print(result)

# 将图片转化为灰度图像
image = image.convert('L')
# image.show()

# 不能直接转化原图，要将原图先转为灰度图像，然后再指定二值化阈值
# 变量 threshold 代表二值化阈值
threshold = 120
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

image = image.point(table, '1')
image.show()
result = tesserocr.image_to_text(image)
print(result)

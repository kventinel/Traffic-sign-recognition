from PIL import Image, ImageDraw
import sys


open_path = sys.argv[1]
save_path = sys.argv[2]
print(open_path, save_path)


def rgb_sum(img, i, j):
    return img[j, i]


def sobel_gradient(img, i, j):
    g_x = - img[j - 1, i - 1] + img[j + 1, i - 1] - \
          2 * img[j - 1, i] + 2 * img[j + 1, i] - \
          img[j - 1, i + 1] + img[j + 1, i + 1]
    g_y = - img[j - 1, i - 1] - 2 * img[j, i - 1] - \
          img[j + 1, i - 1] + img[j - 1, i + 1] + \
          2 * img[j, i + 1] + img[j + 1, i + 1]
    return (g_x ** 2 + g_y ** 2) ** (1 / 2)


image1 = Image.open(open_path).convert('L')
width = image1.size[0]
height = image1.size[1]
image2 = Image.new('L', (width - 2, height - 2))
draw = ImageDraw.Draw(image2)
pix = image1.load()
for i in range(height - 2):
    for j in range(width - 2):
        temp = int(sobel_gradient(pix, i + 1, j + 1))
        if temp > 100:
            temp = 255
        else:
            temp = 0
        draw.point((j, i), temp)

image2.save(save_path, "PPM")
del draw

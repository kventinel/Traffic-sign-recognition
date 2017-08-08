from PIL import Image, ImageDraw
import sys


open_path = sys.argv[1]
save_path = sys.argv[2]
print(open_path, save_path)


def rgb_sum(img, i, j):
    return (img[j, i][0] + img[j, i][1] + img[j, i][2]) / 3


def sobel_gradient(img, i, j):
    g_x = - img[i - 1][j - 1] + img[i - 1][j + 1] - \
          2 * img[i][j - 1] + 2 * img[i][j + 1] - \
          img[i + 1][j - 1] + img[i + 1][j + 1]
    g_y = - img[i - 1][j - 1] - 2 * img[i - 1][j] - \
          img[i - 1][j + 1] + img[i + 1][j - 1] + \
          2 * img[i + 1][j] + matrix[i + 1][j + 1]
    return (g_x ** 2 + g_y ** 2) ** (1 / 2)


image1 = Image.open(open_path)
image2 = Image.open(open_path)
draw = ImageDraw.Draw(image2)
width = image1.size[0]
height = image1.size[1]
pix = image1.load()
matrix = [[0 for j in range(width + 2)] for i in range(height + 2)]
for i in range(height):
    for j in range(width):
        matrix[i + 1][j + 1] = rgb_sum(pix, i, j)
    matrix[i + 1][0] = matrix[i + 1][1]
    matrix[i + 1][width + 1] = matrix[i + 1][width]
for j in range(width + 2):
    matrix[0][j] = matrix[1][j]
    matrix[height + 1][j] = matrix[height][j]
for i in range(height):
    for j in range(width):
        temp = int(sobel_gradient(matrix, i + 1, j + 1))
        if temp > 100:
            temp = 255
        else:
            temp = 0
        draw.point((j, i), (temp, temp, temp))

image2.save(save_path, "PPM")
del draw

from PIL import Image, ImageDraw

def rgb_sum(img, i, j):
    return (img[j, i][0] + img[j, i][1] + img[j, i][2]) / 3


def sobel_gradient (img, i, j, width, height):
    g_x = 0
    g_y = 0
    matrix_x = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    matrix_y = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    if i == 0:
        for t in range(3):
            matrix_x[1][t] += matrix_x[0][t]
            matrix_y[1][t] += matrix_y[0][t]
            matrix_x[0][t] = 0
            matrix_y[0][t] = 0
    if j == 0:
        for t in range(3):
            matrix_x[t][1] += matrix_x[t][0]
            matrix_y[t][1] += matrix_y[t][0]
            matrix_x[t][0] = 0
            matrix_y[t][0] = 0
    if i + 1 == height:
        for t in range(3):
            matrix_x[1][t] += matrix_x[2][t]
            matrix_y[1][t] += matrix_y[2][t]
            matrix_x[2][t] = 0
            matrix_y[2][t] = 0
    if j + 1 == width:
        for t in range(3):
            matrix_x[t][1] += matrix_x[t][2]
            matrix_y[t][1] += matrix_y[t][2]
            matrix_x[t][2] = 0
            matrix_y[t][2] = 0
    for ii in range(3):
        for jj in range(3):
            if matrix_x[ii][jj] != 0:
                g_x += matrix_x[ii][jj] * rgb_sum(img, i + ii - 1, j + jj - 1)
            if matrix_y[ii][jj] != 0:
                g_y += matrix_y[ii][jj] * rgb_sum(img, i + ii - 1, j + jj - 1)
    return (g_x ** 2 + g_y ** 2) ** (1 / 2)


image1 = Image.open("IMG_20170807_005605.jpg")
image2 = Image.open("IMG_20170807_005605.jpg")
draw = ImageDraw.Draw(image2)
width = image1.size[0]
height = image1.size[1]
pix = image1.load()
for i in range(height):
    for j in range(width):
        temp = int(sobel_gradient(pix, i, j, width, height))
        if temp > 30:
            temp = 255
        else:
            temp = 0
        draw.point((j, i), (temp, temp, temp))

image2.save("ans.jpg", "JPEG")
del draw

from math import sqrt
from PIL import Image

MAX_ITER = 50

# def recurrenceMandelbrot(m, c):
#     x, y = m
#     x = x**2 - y**2 + c[0]
#     y = 2*x*y + c[1]
#     return (x, y)

def recurrenceMandelbrot(m, c):
    x, y = m
    m = (x**2 - y**2 + c[0], 2*x*y + c[1])
    return m

def appartientAEnsembleMandelbrot(c):
    z = (0, 0)
    for i in range(MAX_ITER):
        z = recurrenceMandelbrot(z, c)
        if sqrt(z[0]**2 + z[1]**2) > 2:
            return False
    return True

# CORPS DE PROGRAMME
LARG, HAUT = (4000, 4000)
MIN_X, MAX_X = -2, 2
MIN_Y, MAX_Y = -2, 2

coef_x = (MAX_X - MIN_X) / LARG
coef_y = (MAX_Y - MIN_Y) / HAUT

img = Image.new('RGB', (LARG, HAUT), (0, 0, 0))
data = img.load()

for i in range(img.size[0]):
    x = i * coef_x + MIN_X
    for j in range(img.size[1]):
        y = j * coef_y + MIN_Y
        c = (x, y)
        conclusion = appartientAEnsembleMandelbrot(c)
        if conclusion:
            data[i, j] = (255, 255, 255)
        else:
            data[i, j] = (0, 0, 0)

img.save('image.png')
img.show()
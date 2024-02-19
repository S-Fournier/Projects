import numpy as np
from PIL import Image

x=1000
y=1000

img=Image.new('RGB', (x,y))
pixels_matrix=img.load()

def color():
    color_value=np.random.random()*255
    color_value=int(color_value)
    return color_value

for i in range(x):
    for j in range(y):
        pixels_matrix[i,j]=(color(),color(),color())

img.show()
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
img = Image.new( 'RGB', (1000,1500), "black") # create a new black image
pixels = img.load() # create the pixel map

x=1000
y=1500
grid=np.zeros(shape=(x,y))

for i in range(x):
    for j in range(y):
        flip=np.random.uniform(0,1)
        grow=np.random.uniform(0,1)
        if(flip>=0.999):
            grid[i][j]=1
            pixels[i,j]=(255,255,255)
            if(grow>=0.75):
                for a in range(2):
                    for b in range(2):
                        pixels[i-a,j-b]=(255,255,255)
        else:
            pixels[i,j]=(0,0,0)

img.show()
import numpy as np
from PIL import Image


R=50
N=R*2+1
center=int(N/2)
print(center)
blah=np.zeros(shape=(N,N))

img=Image.new('RGB',(N,N),"black")
pixels=img.load()
def fun_cir(x,y,c,r):
    return (x-c)**2+(y-c)**2<=r**2


for i in range(N):  
    for j in range(N):
        if(fun_cir(i,j,center,R)==True):
            pixels[i,j]=(255,255,255)
            blah[i,j]=1

img.show()
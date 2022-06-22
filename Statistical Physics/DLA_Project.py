from PIL import Image
import random
import numpy as np

imgx = 300
imgy = 300
image = Image.new("L", (imgx, imgy))
latticex=np.zeros(imgx)
latticey=np.zeros(imgy)
lattice=np.zeros((imgx,imgy))

nx = [-1, -1, 0, 1, 1, 1, 0, -1]
ny = [0, 1, 1, 1, 0, -1, -1, -1]


def randomstep():
    choose=np.random.uniform(-1,1)
    if choose<0:
        step=1
    if choose>0:
        step=-1
    return step



a=0


while a<2000:
    
    x = np.random.randint(imgx*0.1,imgx*0.9)
    y = np.random.randint(imgx*0.1,imgx*0.9)
    
    
    
    
    b=0    
    while b<1:
        
        x = x + randomstep()
        y = y + randomstep()
        
        
        if image.getpixel((x, y)) == 0:
            
            if x==imgx/2 and y==imgy/2:
                image.putpixel((x,y),255)
                lattice[x,y]=1
                
                b=b+1
                break
            
            
            for k in range(8):
                xn = x + nx[k]
                yn = y + ny[k]
                
                
                
                if xn < 0 or xn > (imgx - 1) or yn < 0 or yn > (imgy - 1):
                    #image.putpixel((x, y), 255)
                    b=b+1
                    break
                
                
                
                if image.getpixel((xn, yn)) > 0:
                    image.putpixel((x, y), 255)
                    lattice[x,y]=1
                    b=b+1
                    break
                
                    
    a=a+1

# test=[]
# for a in range(imgx):
#     for b in range(imgy):
#         if lattice[a,b]==1:
#             test.append(np.mean(lattice[a-10:a+10,b-10:b+10]))
# print np.mean(test)

image.save("DLA_.png", "PNG")
image.show()
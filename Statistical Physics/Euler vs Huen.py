from matplotlib import pyplot as plt
import numpy as np


#Define 1st order ODE

def f(x,y):
    yprime=-(x**2)*y
    return yprime
    
#Define Euler and Heun's Method

def Ey(x0,y0,h):
    x=x0
    y=y0
    while x<1:
        y=y+h*f(x,y)
        x=x+h
    return y
    
# def Hy(x0,y0,h):
#     x=x0
#     y=y0
#     while x<1:
#         y1=y+h*f(x,y)
#         y2=y+0.5*h*(f(x,y)+f(x+h,y1))
#         x=x+h
#         y=y1
#     return y2

    
def Hy(x0,y0,h):
    x=x0
    y1=y0
    y2=y0
    while x<1:
        y1=y1+h*f(x,y1)
        y2=y2+0.5*h*(f(x,y2)+f(x+h,y1))
        x=x+h
    return y2    
                
print(Ey(0,1,0.2))
print(Hy(0,1,0.2))
from types import coroutine
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

def step(s=1):
    theta=np.random.uniform(0,2*np.pi)
    step=np.array([s*np.math.cos(theta),s*np.math.sin(theta)])
    return step

def wall_check(coordinate,step):
    if(coordinate[0]>=20): #hitting right wall
        a=True
        delta=np.array([-1,1])
    elif(coordinate[0]<=0): #hitting left wall
        a=True
        delta=np.array([-1,1])
    elif(coordinate[1]>=20): #hitting top wall
        a=True
        delta=np.array([1,-1])
    elif(coordinate[1]<=0): #hitting bottom wall
        a=True
        delta=np.array([1,-1])
    else:
        a=False
    if(a==True):
        coordinate=coordinate-step

    return coordinate,a

t=0
steps=1000
coordinate_records=np.zeros((steps,2))
coordinate=np.array([10,10])

while t < steps:
    a=step()
    coordinate=coordinate+a
    c=wall_check(coordinate,a)
    if(c[1]==True):
        print("========")
        print(coordinate)
        print(coordinate_records[t-1])
        coordinate=c[0]
        print(coordinate)
    
    
    coordinate_records[t]=coordinate
    t=t+1

for i in range(len(coordinate_records)):
    for j in range(2):
        if(coordinate_records[i][j]>=20 or coordinate_records[i][j]<=0):
            print("=================")
            print("problem coordinate")
            print(coordinate_records[i])
            print("previous position")
            print(coordinate_records[i-1])
            
#print(coordinate_records)       
# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-1, 21), ylim=(-1, 21))
dot, = ax.plot([], [], 'bo', ms=1)

# initialization function: plot the background of each frame
def init():
    dot.set_data([], [])
    return dot,

# animation function.  This is called sequentially
def animate(i):
    x = coordinate_records[i,0]
    y = coordinate_records[i,1]
    dot.set_data(x, y)
    return dot,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=600, interval=200, blit=True)

plt.show()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N=2
Wall=200
t=0
dt=1
T_Stop=300
v=1*dt


#INITIAL CONDITIONS#
ID=np.arange(1,N+1)

Grid=np.zeros(shape=(Wall+10,Wall+10))


x=np.array([90,110])
y=np.array([100,100])

x_record=np.zeros(shape=(N,T_Stop))
y_record=np.zeros(shape=(N,T_Stop))

vx=np.array([1,-1])
vy=np.zeros(N)


while t<T_Stop:
    
    for i in range(N):
        
        x[i]=x[i]+vx[i]

        Hit=False

        #WALL CHECK
    
        a=x[i]>=Wall
        b=y[i]>=Wall
        c=x[i]<=0
        d=y[i]<=0

        if(a or c == True):
            Hit=True
            vx[i]=-vx[i]
        if(b or d == True):
            Hit=True
            vy[i]=-vy[i]
        if(Hit==True):
            
            x[i]=x[i]+vx[i]
            y[i]=y[i]+vy[i]
        
        #END WALL CHECK
        ID_TEMP=ID[i]
        
        Grid[int(x[i]),int(y[i])]
        Grid[int(x[i]),int(y[i])]=Grid[int(x[i]),int(y[i])]+ID_TEMP
        G=Grid[int(x[i]),int(y[i])]
 

        #COLLISION CHECK
        
        if(Grid[int(x[i]),int(y[i])]!=ID_TEMP):
            
            u=int(G-ID_TEMP-1)

            Grid[int(x[i]),int(y[i])]=0

            vx[i]=-1*vx[i]
            vy[i]=-1*vy[i]
            
            x[i]=x[i]+vx[i]
            y[i]=y[i]+vy[i]
            
            vx[u]=-vx[u]
            vy[u]=-vy[u]
            
            x[u]=x[u]+vx[u]
            y[u]=y[u]+vy[u]
        
        #END COLLISION CHECK


    Grid=np.zeros(shape=(Wall+10,Wall+10))
        
    x_record[:,t]=x
    y_record[:,t]=y
    
    t=t+dt









#Animation Section#

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 200), ylim=(0, 200))
dot, = ax.plot([], [], 'bo', ms=1)

# initialization function: plot the background of each frame
def init():
    dot.set_data([], [])
    return dot,

# animation function.  This is called sequentially
def animate(i):
    x = x_record[:,i]
    y = y_record[:,i]
    dot.set_data(x, y)
    return dot,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=300, interval=500, blit=True)

plt.show()
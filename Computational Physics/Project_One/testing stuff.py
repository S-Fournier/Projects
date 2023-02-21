import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#PARAMETERS

N=2000
Bin_N=(N/100)**2
Wall=200
t=0
dt=1
T_Stop=300
v=dt*2
Hits=0
Steps=0
slog=np.zeros(T_Stop)
xaxis=np.arange(0,T_Stop)
a=0

#INITIAL CONDITIONS#


ID=np.arange(1,N+1)

Grid=np.zeros(shape=(Wall+2,Wall+2))
Grid_Bins=Grid

x=np.random.normal(0.5*Wall,5,N)
y=np.random.normal(0.5*Wall,5,N)

theta=np.random.uniform(0,2*np.pi,N)

vx=v*np.cos(theta)
vy=v*np.sin(theta)

x_record=np.zeros(shape=(N,T_Stop))
y_record=np.zeros(shape=(N,T_Stop))

def wall_check(x,y,vx,vy):
    
    Hit=False
    
    a=x>=Wall
    b=y>=Wall
    c=x<=0
    d=y<=0

    if(a or c == True):
        Hit=True
        vx=-vx
    if(b or d == True):
        Hit=True
        vy=-vy
    if(Hit==True):
        
        x=x+vx
        y=y+vy
    
    return x,y,vx,vy

while t<T_Stop:
    
    for i in range(N):
        
        Steps=Steps+1

        x[i]=x[i]+vx[i]
        y[i]=y[i]+vy[i]

        #WALL CHECK

        x[i],y[i],vx[i],vy[i]=wall_check(x[i],y[i],vx[i],vy[i])
    
        #END WALL CHECK

        ID_TEMP=ID[i]
        
        Grid[int(x[i]),int(y[i])]=Grid[int(x[i]),int(y[i])]+ID_TEMP
        Grid_Bins[int(x[i]),int(y[i])]=Grid_Bins[int(x[i]),int(y[i])]+1
        G=Grid[int(x[i]),int(y[i])]

        #COLLISION CHECK
        
        if(Grid[int(x[i]),int(y[i])]!=ID_TEMP):
            
            Hits=Hits+1
            
            u=int(G-ID_TEMP-1)

            Grid[int(x[i]),int(y[i])]=0
            Grid_Bins[int(x[i]),int(y[i])]=0

            vx[i]=-1*vx[i]
            vy[i]=-1*vy[i]
            
            x[i]=x[i]+vx[i]
            y[i]=y[i]+vy[i]
            
            #WALL CHECK
            x[i],y[i],vx[i],vy[i]=wall_check(x[i],y[i],vx[i],vy[i])
            #END WALL CHECK

            vx[u]=-vx[u]
            vy[u]=-vy[u]
            
            x[u]=x[u]+vx[u]
            y[u]=y[u]+vy[u]
            
            #WALL CHECK
            x[u],y[u],vx[u],vy[u]=wall_check(x[u],y[u],vx[u],vy[u])
            #END WALL CHECK

        #END COLLISION CHECK

    s=0
    for i in range(20):
        box_sum=np.sum(Grid_Bins[10*i:10*(i+1),10*i:10*(i+1)])
        p=box_sum/N
        #print(box_sum)
        
        if(p>0):
            s=s+p*np.log(p)
    s=-s
    slog[a]=s

    x_record[:,t]=x
    y_record[:,t]=y
    
    Grid=np.zeros(shape=(Wall+2,Wall+2))

    a=a+1
    t=t+dt

print(Hits,'/',Steps)
print(Hits/Steps)
print(N*Hits/Steps)

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
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=300, interval=200, blit=True)

#plt.plot(xaxis,slog,'.')
plt.show()
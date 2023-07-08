import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.special import erf
import math

#PARAMETERS
Hits=0
Steps=0
N=1000
Wall=1000
t=0
T_Stop=300
xaxis=np.arange(0,T_Stop)

k_B=1.38*10**(-23) #Boltzmann constant (J/K)
m_H=1.67*10**(-24) #Mass of hydrogen (kg)
T_K=300  #Temperature (K)
v_th=np.sqrt(k_B*T_K/m_H)  #Thermal velocity

#INITIAL CONDITIONS

def boltzmann_velocities(u):
    v=v_th*np.sqrt(-2*np.log(1-u))
    return v

u=np.random.uniform(0,1,N)
v=boltzmann_velocities(u)/10
Buffer=int(np.amax(v))

#Arrays of particle x and y coordinates

distribution='uniform'

if(distribution=='normal'):
    x=np.random.normal(0.5*Wall,20,N)
    y=np.random.normal(0.5*Wall,20,N)

elif(distribution=='uniform'):
    x_portion=1
    y_portion=1
    x=np.random.uniform(Buffer,x_portion*Wall-Buffer,N)
    y=np.random.uniform(Buffer,y_portion*Wall-Buffer,N)

#Array of particle velocities in x and y directions

theta=np.random.uniform(0,2*np.pi,N)

vx=v*np.cos(theta)
vy=v*np.sin(theta)

#Records
s_record=np.zeros(T_Stop) #entropy
p_record=np.zeros(T_Stop) #pressure
x_record=np.zeros(shape=(N,T_Stop)) #x coordinates
y_record=np.zeros(shape=(N,T_Stop)) #y coordinates
vx_record=np.zeros(shape=(N,T_Stop)) #velocities in x direction
vy_record=np.zeros(shape=(N,T_Stop)) #velocities in y direction
hit_record=np.zeros(shape=(N,T_Stop)) #hits
free_record=np.zeros(N)

#GRID AND ID SETUP
ID=np.arange(1,N+1)
Grid=np.zeros(shape=(Wall+Buffer,Wall+Buffer))
Grid_Bins=Grid


def wall_check(x,y,vx,vy,p_record):
    
    Hit=False
    
    #Boolean check#
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
    
    vmag=np.sqrt(vx**2+vy**2)

    p_record=p_record+2*vmag
    
    return x,y,vx,vy,p_record

while t<T_Stop:
    
    for i in range(N):

        Steps=Steps+1

        x[i]=x[i]+vx[i]
        y[i]=y[i]+vy[i]

        free_record[i]=free_record[i]+1

        #WALL CHECK

        x[i],y[i],vx[i],vy[i],p_record[t]=wall_check(x[i],y[i],vx[i],vy[i],p_record[t])
    
        #END WALL CHECK

        ID_TEMP=ID[i]
        
        Grid[int(x[i]),int(y[i])]=Grid[int(x[i]),int(y[i])]+ID_TEMP
        Grid_Bins[int(x[i]),int(y[i])]=Grid_Bins[int(x[i]),int(y[i])]+1
        G_TEMP=Grid[int(x[i]),int(y[i])]

        #COLLISION CHECK
        
        if(Grid[int(x[i]),int(y[i])]!=ID_TEMP):
            
            Hits=Hits+2

            u=int(G_TEMP-ID_TEMP-1)

            Grid[int(x[i]),int(y[i])]=0
            Grid_Bins[int(x[i]),int(y[i])]=0

            vx[i],vx[u]=-vx[u],-vx[i]
            vy[i],vy[u]=-vy[u],-vy[i]
            
            x[i]=x[i]+vx[i]
            y[i]=y[i]+vy[i]
            x[u]=x[u]+vx[u]
            y[u]=y[u]+vy[u]
            
            #WALL CHECK
            x[i],y[i],vx[i],vy[i],p_record[t]=wall_check(x[i],y[i],vx[i],vy[i],p_record[t])
            x[u],y[u],vx[u],vy[u],p_record[t]=wall_check(x[u],y[u],vx[u],vy[u],p_record[t])
            #END WALL CHECK
            hit_record[i,t]=free_record[i]
            hit_record[u,t]=free_record[u]
            free_record[i]=0
            free_record[u]=0


        #END COLLISION CHECK


    #CALCULATE ENTROPY
    s=0
    for i in range(20):
        box_sum=np.sum(Grid_Bins[10*i:10*(i+1),10*i:10*(i+1)])
        p=box_sum/N
        if(p>0):
            s=s+p*np.log(p)
    s=-s
    
    #RECORD
    s_record[t]=s
    x_record[:,t]=x
    y_record[:,t]=y
    vx_record[:,t]=vx
    vy_record[:,t]=vy
    
    #RESET GRID
    Grid=np.zeros(shape=(Wall+Buffer,Wall+Buffer))

    t=t+1

vmag=np.sqrt(vx_record**2+vy_record**2)
nonzero_indices = np.nonzero(hit_record)
mean_time=np.mean(hit_record[nonzero_indices])
mean_v=np.mean(vmag)

#Animation Section#

option=0

if(option==0):
    # First set up the figure, the axis, and the plot element we want to animate
    fig = plt.figure()
    ax = plt.axes(xlim=(0-(Wall/10), Wall+(Wall/10)), ylim=(0-(Wall/10), Wall+(Wall/10)))
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
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=T_Stop, interval=200, blit=True)
elif(option==1):
    plt.plot(xaxis,s_record,'.')
plt.show()

#COMPARE TIME FOR NESTED FOR LOOP AND GRID DETECTION SYSTEM
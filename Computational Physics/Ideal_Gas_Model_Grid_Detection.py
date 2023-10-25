import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.special import erf

#OPTIONS
distribution='normal' #normal or uniform
plot='animation' #animation, entropy or pressure
save='no' #save the animation

#PARAMETERS
N=1000 #number of particles
Wall=10000 #box size
time_stop=300 #number of steps
time_axis=np.arange(0,time_stop) #range of steps
s=0 #entropy variable initialization
cell=int(Wall/100) #cell size
v_k=1 #constant affecting velocity
k_B=1.38*10**(-23) #boltzmann constant (J/K)
m_H=1.67*10**(-24) #mass of hydrogen (kg)
T_K=300  #temperature (K)
v_th=np.sqrt(k_B*T_K/m_H)  #thermal velocity

#INITIAL CONDITIONS

def boltzmann_velocities(mu):
    v=v_k*v_th*np.sqrt(-2*np.log(1-mu)) #distribution of velocities given by the boltzman equation
    return v

mu=np.random.uniform(0,1,N) #array of random input variables for the distribution
v=boltzmann_velocities(mu) #velocities picked from distrubution using mu
Buffer=int(np.amax(v)) #buffer zone to prevent particles from going out of range
theta=np.random.uniform(0,2*np.pi,N)
vx=v*np.cos(theta) #velocity in x direction
vy=v*np.sin(theta) #velocity in y direction

if(distribution=='normal'):
    x=np.random.normal(0.5*Wall,20,N)
    y=np.random.normal(0.5*Wall,20,N)

elif(distribution=='uniform'):
    x=np.random.uniform(Buffer,Wall-Buffer,N)
    y=np.random.uniform(Buffer,Wall-Buffer,N)

#RECORDS
s_record=np.zeros(time_stop)
p_record=np.zeros(time_stop)
x_record=np.zeros(shape=(N,time_stop))
y_record=np.zeros(shape=(N,time_stop))

#GRID AND ID SETUP
ID=np.arange(1,N+1)
Grid=np.zeros(shape=(Wall+Buffer,Wall+Buffer)) #the position grid where the particles place their ID flags
Grid_Bins=np.zeros(shape=(Wall+Buffer,Wall+Buffer)) #bins 

def wall_check(x,y,vx,vy,p_record,m_H):
    
    Hit=False
    
    #BOOLEAN CHECK#
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

        p_record=p_record+2*m_H*vmag
    
    return x,y,vx,vy,p_record

#START SIMULATION

for t in range(time_stop):
    
    #ACTIONS IN TIME STEP t

    for i in range(N):
        
        #MOVE PARTICLE i

        x[i]=x[i]+vx[i]
        y[i]=y[i]+vy[i]

        #WALL CHECK

        x[i],y[i],vx[i],vy[i],p_record[t]=wall_check(x[i],y[i],vx[i],vy[i],p_record[t],m_H)
    
        #END WALL CHECK

        #PLACE GRID MARKER
        
        Grid[int(x[i]),int(y[i])]=Grid[int(x[i]),int(y[i])]+ID[i]
        Grid_Bins[int(x[i]),int(y[i])]=Grid_Bins[int(x[i]),int(y[i])]+1

        #COLLISION CHECK
        
        if(Grid[int(x[i]),int(y[i])]!=ID[i]):

            u=int(Grid[int(x[i]),int(y[i])]-ID[i]-1)

            vx[i],vx[u]=vx[u],vx[i]
            vy[i],vy[u]=vy[u],vy[i]

            Grid[int(x[i]),int(y[i])]=0

        #END COLLISION CHECK

    #CALCULATE ENTROPY
    if(plot=='entropy'):
        for a in range(cell):
            for b in range(cell):
                Bin=0
                for i in range(cell):
                    for j in range(cell):
                        Bin=Bin+Grid_Bins[cell*a+i][cell*b+j]
                p=Bin/N
                if(p>0):
                    s=s-p*np.log(p)
                p=0
    
    #RECORD
    s_record[t]=s
    x_record[:,t]=x
    y_record[:,t]=y
    
    #RESET
    Grid=np.zeros(shape=(Wall+Buffer,Wall+Buffer))
    Grid_Bins=np.zeros(shape=(Wall+Buffer,Wall+Buffer))
    s=0

#END SIMULATION

#DISPLAYING SIMULATION DATA

if(plot=='animation'):
    fig=plt.figure()
    ax=plt.axes(xlim=(0-(Wall/10),Wall+(Wall/10)),ylim=(0-(Wall/10),Wall+(Wall/10)))
    plt.axis('off')
    rectangle=plt.Rectangle((0,0),Wall,Wall,fc='white',ec="red")
    plt.gca().add_patch(rectangle)
    dot,=ax.plot([],[],'bo',ms=1)

    def init():
        dot.set_data([],[])
        return dot,

    def animate(i):
        x=x_record[:,i]
        y=y_record[:,i]
        dot.set_data(x, y)
        return dot,

    anim=animation.FuncAnimation(fig,animate,init_func=init,frames=time_stop,interval=200,blit=True)
    if(save=='yes'):
        anim.save('test1.gif')

elif(plot=='entropy'):
    plt.plot(time_axis,s_record,'.')

elif(plot=='pressure'):
    plt.plot(time_axis,p_record,'.')
plt.show()
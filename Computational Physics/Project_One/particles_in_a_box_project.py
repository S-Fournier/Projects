import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation


#Takes a coordinate and a grid and adds it to a 2D histogram
def count(x,y,a,b,c):
    for i in range(len(a)):
        
        if(x<a[i] and x>a[i]-2):
        
            for j in range(len(b)):
                
                if(y<b[j] and y >b[j]-2):
                    
                    c[i][j]=c[i][j]+1
    return c

#Creates the inital starting positions for the particles.
def initial_placement(side,N):
    
    x=np.random.normal(side*0.5,0.5,N)
    y=np.random.normal(side*0.5,0.5,N)
    coordinates=np.array([x,y])
    return coordinates

#Sets up arguments for count function and creates a 2D histogram using the given set of coordinates
def box_histo(coordinates,side,cell,N):
    
    unit=int((side/cell))
    xgrid=np.linspace(cell,side,unit)
    ygrid=np.linspace(cell,side,unit)
    grid=np.zeros((unit,unit))
    
    for i in range(N):
        count(coordinates[0][i],coordinates[1][i],xgrid,ygrid,grid)
    
    return grid

#Takes the histogram and defines the probability as the number of particles in a cell over the total particles
#Finds entropy as a function of probability 
def entropy(grid,particles):
    
    s=0
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            p=grid[i][j]/particles
            if(p==0):
                s=s+0
            else:
                s=s+p*np.log(p)
    s=s*-1
    return s

#Modeling collisions based off of MFP and current entropy
#Essentially a BOOL generator with a probability of it being TRUE in proportion to entropy
def collision(dt,MFP,entropy):
    ''' if(entropy>1.3 and entropy<2.0):
        c=0.25
    elif(entropy>2.0 and entropy<2.7):
        c=0.175
    elif(entropy>2.7 and entropy<3.3):
        c=0.1
    elif(entropy>3.3 and entropy<4.0):
        c=0
    elif(entropy>4.0):
        c=0 '''
    p_of_collision=(dt/MFP)
    u=np.random.uniform(0,1)
    if(u<p_of_collision):
        a=True
    else:
        a=False
    return a

#Checks a particle's position to see if it hits the barrier
#If it hits the barrier, reflect the particle based on its previous position 
def wall_check(coordinate,t,hit_count,step):
    if(coordinate[0]>=20 and coordinate[1]>=20): #hitting corner
        a=True
        delta=np.array([-1,-1])
    elif(coordinate[0]<=0 and coordinate[1]<=0):
        a=True
        delta=np.array([-1,-1])
    elif(coordinate[0]>=20): #hitting right wall
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
        hit_count[t]=hit_count[t]+1

        coordinate=coordinate-step
        
    return coordinate,hit_count,a

#Function that generates a random step for a particle to take
def step(s=1):
    theta=np.random.uniform(0,2*np.pi)
    step=np.array([s*np.math.cos(theta),s*np.math.sin(theta)])
    return step

#N->number of particles
#Z->total time allowed
#dt->step size
#t->step number
#dF->2*m*v=2 for hydrogen and 2*14*1/sqrt(14) for nitrogen
#(FIXED) Knowing when the particles are at equilibrium seems to be the biggest challege. Not only does entropy not reach an ideal value, but the value seems to decrease after a certain point.


#dt might need to be fine tuned. 0.5 Seems to be a bit fast which makes calculating the equilibrium harder
def go():
    N=10000
    Z=10000
    dt=0.5
    t=0
    dS=100
    hit_count=np.zeros(Z)
    coordinates=initial_placement(20,N)
    
    S=entropy(box_histo(coordinates,20,2,N),N)
    T=np.zeros(Z) #timestamp array
    
    #Array to keep track of coordinates
    track=np.zeros(shape=(2,N,Z))
    track[:,:,0]=coordinates
    
    while dS > 0.001 or dS < 0:
        t=t+1 #step number
        T[t]=T[t-1]+dt 
        
        for i in range(N):
            delta=step()*dt
            coordinates[:,i]=coordinates[:,i]+delta
            check=wall_check(coordinates[:,i],t,hit_count,delta)
            coordinates[:,i]=check[0]
            check_bool=check[2]
            if(collision(dt,1,S)==True and check_bool==False):
                delta=step()*dt
                coordinates[:,i]=coordinates[:,i]+delta
        
        track[:,:,t]=coordinates #saves coordinate on the index according to step number
        S_Temp=entropy(box_histo(coordinates,20,2,N),N)
        dS=S_Temp-S
        S=S_Temp
        print(S)
    return track

positions=go()
print(np.shape(positions))
#Animation Section#

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 20), ylim=(0, 20))
dot, = ax.plot([], [], 'bo', ms=1)

# initialization function: plot the background of each frame
def init():
    dot.set_data([], [])
    return dot,

# animation function.  This is called sequentially
def animate(i):
    x = positions[0,:,i]
    y = positions[1,:,i]
    dot.set_data(x, y)
    return dot,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=600, interval=200, blit=True)

plt.show()
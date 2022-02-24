import numpy as np
import matplotlib.pyplot as plt
import random

def random_step1D():
    choose=np.random.uniform(-1,1)
    if choose<0:
        choose=-1.0
    if choose>0:
        choose=1.0
    return choose

def random_step2D(s=1):
    theta=np.random.uniform(0,2*np.pi)
    x=s*np.math.cos(theta)
    y=s*np.math.sin(theta)
    return x,y,theta

def walk1D(N):
    step=0
    d=0
    while(step<N):
        d=d+random_step1D()
        step=step+1
    return d

def walk2D(N):
    step=0
    x=0
    y=0
    d=0
    xrec=np.zeros(N)
    yrec=np.zeros(N)
    while(step<N):
        random=random_step2D()
        x=x+random[0]
        y=y+random[1]
        xrec[step]=x
        yrec[step]=y
        d=np.sqrt(x**2+y**2)
        step=step+1
    return x,y,xrec,yrec,d

def walknbox(N,s,wall):
    x=0
    y=0
    step=0
    xrec=np.zeros(N)
    yrec=np.zeros(N)
    while(step<N):
        if(x>=wall or x<=(wall*-1)):
            x=xrec[step-2]
            y=y+random[1]
            xrec[step]=x
            yrec[step]=y
        elif(y>wall or y<(wall*-1)):
            x=x+random[0]
            y=yrec[step-2]
            xrec[step]=x
            yrec[step]=y
        else:
            random=random_step2D(s)
            x=x+random[0]
            y=y+random[1]
            xrec[step]=x
            yrec[step]=y
        step=step+1
    return x,y,xrec,yrec

def entropyboxes(xlength,ylength,cell,particles):
    x=np.linspace(0,xlength,xlength/cell)
    y=np.linspace(0,ylength,ylength/cell)
    grid=np.zeros((xlength,ylength))
    xps=np.random.uniform(0.,xlength,particles)
    yps=np.random.uniform(0.,ylength,particles)
    
    for a in range(particles):
        count(xps[a],yps[a],x,y,grid)
    return grid
    
def count(x,y,a,b,c):
    for i in range(len(a)):
        
        if(x<a[i] and x>a[i]-2):
        
            for j in range(len(b)):
                
                if(y<b[j] and y >b[j]-2):
                    
                    c[i][j]=c[i][j]+1
    return c

def box_random(xlength,ylength,cell,particles,type):
    
    xunit=int((xlength/cell))
    yunit=int((ylength/cell))
    
    xgrid=np.linspace(cell,xlength,xunit)
    ygrid=np.linspace(cell,ylength,yunit)
    
    grid=np.zeros((xunit,yunit))
    
    if(type=="uniform"):
        x=np.random.uniform(0.,xlength,particles)
        y=np.random.uniform(0.,ylength,particles)
    
    elif(type=="normal"):
        x=np.random.normal(xlength/2,3,particles)
        y=np.random.normal(ylength/2,3,particles)
    
    for a in range(particles):
        count(x[a],y[a],xgrid,ygrid,grid)
    
    return grid

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

def test():
    box=box_random(20,20,2,1000,'normal')
    S=entropy(box,1000)
    return box,S

def mean_std(N):
    summ=0
    delta=0
    a=np.zeros(N)
    for i in range(N):
        box=box_random(20,20,2,1000,'uniform')
        S=entropy(box,1000)
        a[i]=S
        summ=summ+S
    mean=summ/N
    
    for j in range(N):
        delta=delta+(a[j]-mean)**2
    std=np.sqrt(delta/N)
    
    return mean,std

def units():
    v_H=1
    m_H=1
    m_N=14
    v_N=v_H*np.sqrt(m_H/m_N)
    Entropy_Mean=4.554889889220872
    Entropy_STD=0.0071168935712729265
    return v_H,m_H,m_N,v_N,Entropy_Mean,Entropy_STD

def collision(dt,MFP,entropy):
    if(entropy>1.3 and entropy<2.0):
        c=0.25
    elif(entropy>2.0 and entropy<2.7):
        c=0.175
    elif(entropy>2.7 and entropy<3.3):
        c=0.1
    elif(entropy>3.3 and entropy<4.0):
        c=0
    elif(entropy>4.0):
        c=0
    p_of_collision=(dt/MFP)+c
    u=np.random.uniform(0,1)
    if(u<p_of_collision):
        a=True
    else:
        a=False
    return a

def center_placement(N):
    
    H_coordinates=np.zeros((N,2))
    N_coordinates=np.zeros((N,2))
    H_coordinates[:,0]=np.random.normal(10,0.5,N)
    H_coordinates[:,1]=np.random.normal(10,0.5,N)
    N_coordinates[:,0]=np.random.normal(10,0.5,N)
    N_coordinates[:,1]=np.random.normal(10,0.5,N)
    
    return H_coordinates,N_coordinates

def store(wall,dt,hit_count):
    if(wall==1):
        hit_count[dt]=hit_count[dt]+1
    return hit_count

def wall_check(coordinate,dt,hit_count,step):
    if(coordinate[0]>=20):
        a=True
        delta=np.array([[-1],[1]])
    elif(coordinate[0]<=0):
        a=True
        delta=np.array([[-1],[1]])
    elif(coordinate[1]>=20):
        a=True
        delta=np.array([[1],[-1]])
    elif(coordinate[1]<=0):
        a=True
        delta=np.array([[1],[-1]])
    else:
        a=False
    if(a==True):
        hit_count[dt]=hit_count[dt]+1
        coordinate=coordinate+step*delta
    return coordinate,hit_count

def move(coordinate,delta,step,T,hit_count):
    coordinate=coordinate+step*delta
    store(1,T,hit_count)
    return coordinate,hit_count

def step(s=1):
    theta=np.random.uniform(0,2*np.pi)
    step=np.array([s*np.math.cos(theta),s*np.math.sin(theta)])
    return step

def box_initial(side,cell,particles):
    
    unit=int((side/cell))
    xgrid=np.linspace(cell,side,unit)
    ygrid=np.linspace(cell,side,unit)
    grid=np.zeros((unit,unit))
    
    coordinates=center_placement(particles)
    H_coordinates=coordinates[0]
    N_coordinates=coordinates[1]
    
    for a in range(particles):
        count(H_coordinates[a][0],H_coordinates[a][1],xgrid,ygrid,grid)
        count(N_coordinates[a][0],N_coordinates[a][1],xgrid,ygrid,grid)
    
    return grid

def box_histo(H_coordinates,N_coordinates,side,cell,particles):
    
    unit=int((side/cell))
    xgrid=np.linspace(cell,side,unit)
    ygrid=np.linspace(cell,side,unit)
    grid=np.zeros((unit,unit))
    
    for a in range(particles):
        count(H_coordinates[a][0],H_coordinates[a][1],xgrid,ygrid,grid)
        count(N_coordinates[a][0],N_coordinates[a][1],xgrid,ygrid,grid)
    
    return grid

def go():
    N=1000
    Z=10000
    v_N=1/np.sqrt(14)
    hit_count=np.zeros(Z)
    coordinates=center_placement(500)
    H_coordinates=coordinates[0]
    N_coordinates=coordinates[1]
    S=entropy(box_initial(20,2,500),N)
    S_list=np.zeros(Z)
    T=np.zeros(Z)
    dt=0.1
    i=0
    H_track=np.zeros(shape=(500,2,len(T)))
    H_track[:,:,0]=H_coordinates
    N_track=np.zeros(shape=(500,2,len(T)))
    N_track[:,:,0]=N_coordinates
    dS=100
    while dS > 0.0000000000000000000000000000000000001:
        i=i+1
        T[i]=T[i-1]+dt
        for a in range(len(H_coordinates)):
            delta=step()*dt
            H_coordinates[a]=H_coordinates[a]+delta
            if(collision(dt,1,S)==True):
                H_coordinates[a]=H_coordinates[a]+delta
            wall_check(H_coordinates[a],i,hit_count,delta)
        for b in range(len(N_coordinates)):
            delta=step(v_N)*dt
            N_coordinates[b]=N_coordinates[b]+delta
            if(collision(dt,1,S)==True):
                N_coordinates[b]=N_coordinates[b]+delta
            wall_check(N_coordinates[a],i,hit_count,delta)
        H_track[:,:,i]=H_coordinates
        N_track[:,:,i]=N_coordinates
        A=entropy(box_histo(H_coordinates,N_coordinates,20,2,500),N)
        if(i>100):
            dS=S-A
            S=A
        S=A
        print(S,H_coordinates[0])

#NEEDED TO DO THEM SEPERATELY

#invert positions
#1.3-2.0: +0.25
#2.0-2.7: +0.175
#2.7-3.3: +0.1
#3.3-4.0: +0.025
#4.038744513967448, [3.625770928172323 3.282517399944093], [2.626609742196879, 2.0497490077317186], 1.3846615343626163
#TIME STEPS SHOULD BE SMALL AKA DT<<1
#lower the entropy the higher the chance of a collision [+0.5,+0.375,+0.25,+0.125]
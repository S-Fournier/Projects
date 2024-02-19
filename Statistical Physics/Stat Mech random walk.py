import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import random

Z=1000
N=100
distance=np.zeros(Z)

def walk(start,A):
    for b in range(Z):
        step=start
        for c in range(N):
            choose=np.random.uniform(-1,1)
            if choose<0:
                step=step-1.
            if choose>0:
                step=step+1.
        distance[b]=step**A
    u=np.sum(distance)/Z
    return u
    
#print walk(0,1)
#print np.sqrt(walk(0,2))
#print np.sqrt(100)





def borderwalk(start,L):
    
    left=0
    
    for b in range(Z):
        
        step=start
        
        for c in range(N):
            
            if step<=0.:
                left=left+1
                break

            #if step>=L:
             #   break

            choose=np.random.uniform(-1.,1.)

            if choose<0.:
                step=step-1.

            if choose>0.:
                step=step+1.

    return left/float(Z)




space=100
startlist=np.linspace(0,1,space)
border1=5
border2=10
border3=15
border4=20
border5=25

prob1=np.zeros(space)
prob2=np.zeros(space)
prob3=np.zeros(space)
prob4=np.zeros(space)
prob5=np.zeros(space)

for a in range(space):
    prob1[a]=borderwalk(startlist[a]*border1,border1)
    prob2[a]=borderwalk(startlist[a]*border2,border2)
    prob3[a]=borderwalk(startlist[a]*border3,border3)
    prob4[a]=borderwalk(startlist[a]*border4,border4)
    prob5[a]=borderwalk(startlist[a]*border5,border5)

print prob1
print prob2
print prob3

A=plt.subplot(111)
A.set_title('L=10')
A.set_xlabel('x0')
A.set_ylabel('P(x0)')


#plt.plot(startlist,prob1,'.')
#plt.plot(startlist,prob2,'.')
#plt.plot(startlist,prob3,'.')
#plt.plot(startlist,prob4,'.')
#plt.plot(startlist,prob5,'.')

plt.show()
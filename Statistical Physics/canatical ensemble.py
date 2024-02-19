import numpy as np

N=20
Z=100
k=1
T=300
B=1/(k*T)

E=np.zeros(Z)
E0=N*T+np.random.uniform(-5,5)
Ebar=np.zeros(N)

#Define Functions#

def P(s):

    P=np.exp(-B*s)

    return P
    
def randomstep():
    choose=np.random.uniform(-1.,1.)
    return choose


#Random walk with E0 around NT

for a in range(N):
    
    for i in range(Z):
    
        delta=randomstep() 

        if(delta>0):

            if(delta>P(delta)):

                E[i]=E[i-1]
                
        else:
            
            E[i]=E0-delta

        E0=E[i]
        
    Ebar[a]=np.average(P(E))
    

print(Ebar)
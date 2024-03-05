import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

neighbor=np.array([-1,1])
n=50000
size=50
time_axis=np.arange(0,n)
Z=np.zeros(shape=(size,size))
Z_record=np.zeros(shape=(n,size,size))
count=np.zeros(n)
option='animate'
save=False
save_name='soc_1.2.gif'

def chi2(x,y,p):
    X2=0
    for i in range(len(x)):
        E_i=x[i]**p
        O_i=y[i]
        X2=X2+((O_i-E_i)**2)/E_i
    return X2

def fit(x,y,p0,cutoff,gamma):
    p=p0
    end=False
    if(chi2(x,y,p+gamma)>chi2(x,y,p-gamma)):
            gamma=gamma*-1
    while end==False:
        dX2=(chi2(x,y,p+gamma)-chi2(x,y,p))/gamma
        if(dX2<cutoff):
            end=True
        p=p+gamma    
    return p

def check(Z,row,column):
    if(Z[row,column]==4):
        Z[row,column]=0
        count[step]=count[step]+4
        for i in range(len(neighbor)):
            dx=row+neighbor[i]
            if dx >= 0 and dx < size:
                Z[dx,column]=Z[dx,column]+1
                check(Z,dx,column)
        for j in range(len(neighbor)):
            dy=column+neighbor[j]
            if dy >= 0 and dy < size:
                Z[row,dy]=Z[row,dy]+1
                check(Z,row,dy)
    return Z

for step in range(0,n):
    row=np.random.randint(0,size)
    column=np.random.randint(0,size)
    Z[row,column]=Z[row,column]+1
    check(Z,row,column)
    Z_record[step,:,:]=Z

if option=='animate':
    fig, ax = plt.subplots()
    im=plt.imshow(Z_record[0,:,:],vmin=0,vmax=3)
    ax.axis('off')
    plt.colorbar
    def animate(i):
        im.set_data(Z_record[i,:,:])
    anim=animation.FuncAnimation(fig,animate,frames=n,interval=5)
    if save==True:
        anim.save(save_name)
    plt.show()

if option=='histogram':
    count=count[5000:]
    sample=np.sort(count)
    sample=sample[np.where(sample>1)]
    sample=sample[np.where(sample<100)]
    
    bins=np.unique(sample) #x axis
    bin_values=np.array([0]) #y axis
    
    j=0
    for i in range(1,len(sample)):
        if sample[i-1]==sample[i]:
            bin_values[j]=bin_values[j]+1
        else:
            bin_values=np.append(bin_values,1)
            j=j+1
    
    bin_values=bin_values/len(sample)
    bin_values_p=fit(bins,bin_values,-1,0.001,0.01)
    bin_values_fit=(bins)**(bin_values_p)

    plt.plot(bins,bin_values,'-',label='Avalanche Size')
    plt.plot(bins,bin_values_fit,'--',label='p='+str(bin_values_p))
    plt.legend()
    plt.xlabel('Avalanche Size')
    plt.ylabel('Frequency')
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
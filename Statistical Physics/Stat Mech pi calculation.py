import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import random

Z=1000
N=10000
pi=np.zeros(Z)

for b in range(Z):
    A=0
    for i in range(N):
        x=np.random.uniform(-1,1)
        y=np.random.uniform(-1,1)
        C=x**2+y**2
        if C<=1:
            A=A+1.0
    pi[b]=4.0*A/N

pimean=np.average(pi)
#sigma=np.sqrt(1./N)
sigma=np.std(pi)
bins=np.linspace(pimean-3*sigma,pimean+3*sigma,Z)

print(pimean)

plt.plot(bins,mlab.normpdf(bins, pimean, sigma))
plt.hist(pi, 30, facecolor='red', alpha=0.5)
plt.show()
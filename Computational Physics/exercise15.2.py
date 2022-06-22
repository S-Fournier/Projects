import numpy as np
import matplotlib.pyplot as plt

z=np.array([-1.,0.,-2.,2.,1.])
amp=np.array([2.23,3.02,0.982,2.00,2.92])
sigma=np.array([0.03, 0.03, 0.025, 0.029, 0.03])

M=np.array([[1,z[0],z[0]**2],[1,z[1],z[1]**2],[1,z[2],z[2]**2],[1,z[2],z[3]**2],[1,z[2],z[4]**2]])

Mt=M.transpose()

alpha=np.dot(Mt,M)

invalpha=np.linalg.inv(alpha)

iden=np.dot(invalpha,alpha)

amp_prime=amp/sigma

p=np.dot(invalpha,np.dot(Mt,amp))

print(p)

ampfit=p[2]+p[1]*z+p[0]*z**2

plt.errorbar(z,amp,yerr=sigma,fmt='.')
plt.plot(z,ampfit,".")
plt.show()
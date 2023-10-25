import numpy as np
import matplotlib.pyplot as plt

#collect your N-data points, 𝑥 and 𝑦, in numpy arrays
#x
z=np.array([-1.,0.,-2.,2.,1.])
#y
amp=np.array([2.23,3.02,0.982,2.00,2.92])
#determine errors
sigma=np.array([0.03, 0.03, 0.025, 0.029, 0.03])


#construct M matrix
M=np.zeros(shape=(len(z),3))
for i in range(len(z)):
    M[i,0]=1
    M[i,1]=z[i]
    M[i,2]=(z[i]**2)

#transpose matrix
Mt=M.transpose()

#construct alpha matrix
alpha=np.dot(Mt,M)

#construct the inverse of alpha
alpha_inv=np.linalg.inv(alpha)

#construct the vector y' with y/sigma
amp_prime=amp/sigma

#best fit paramaters are p=alpha*Mt*y'
b=np.dot(Mt,amp)
p=np.dot(alpha_inv,b)

print(p)

ampfit=p[0]+p[1]*z+p[2]*z**2

x=np.linspace(-2,2)
y=p[0]+p[1]*x+p[2]*x**2

plt.errorbar(z,amp,yerr=sigma,fmt='.')
plt.plot(z,ampfit,"o")
plt.plot(x,y,'--')
plt.show()
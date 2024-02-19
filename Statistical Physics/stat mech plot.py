import numpy as np
import matplotlib.pyplot as plt


N=np.linspace(100.,10000.,10000)
sigma=1./np.sqrt(N)

A=plt.subplot(111)
A.set_xscale('log')
A.set_yscale('log')
A.set_title('Convergence of Sigma as N goes to Infinity')
A.set_xlabel('N')
A.set_ylabel(r'$\sigma$')

plt.plot(N,sigma)
plt.show()
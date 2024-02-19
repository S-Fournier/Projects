import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,20)
yint=0
slope=float(raw_input("slope="))

y=x*slope

noise=np.random.normal(0,2,len(x))

ynoise=y+noise

chi2=0
for i in range(len(x)):

	cha=(y[i]-ynoise[i])**2/4
	chi2+=cha

print chi2
#plt.plot(x,y)
#plt.show()
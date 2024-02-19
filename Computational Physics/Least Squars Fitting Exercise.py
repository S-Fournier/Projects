import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

def Sigma(variable):
    SUM=0
    for i in range(len(variable)):
        SUM=SUM+variable[i]
    return SUM

def FIT(x,y):
    
    def find_a(sx,sx2,sxy,sy,N):
        a0=(sx2*sy)/D
        a1=(-sx*sxy)/D
        a=a0+a1
        return a
    
    def find_b(sx,sx2,sxy,sy,N):
        b0=(-sx*sy)/D
        b1=(N*sxy)/D
        b=b0+b1
        return b
    
    N=len(x)
    Sigma_x=Sigma(x)
    Sigma_x2=Sigma(x**2)
    Sigma_y=Sigma(y)
    Sigma_xy=Sigma(x*y)
    D=N*Sigma_x2-Sigma_x**2
    
    a=find_a(Sigma_x,Sigma_x2,Sigma_xy,Sigma_y,N)
    b=find_b(Sigma_x,Sigma_x2,Sigma_xy,Sigma_y,N)

    sigma2=1
    sigma2_a=(sigma2*Sigma_x2)/D
    sigma2_b=(sigma2*N)/D
    sigma2_ab=(sigma2*-Sigma_x)/D

    cov_matrix=np.array([(sigma2_a,sigma2_ab),(sigma2_ab,sigma2_b)])
    
    return a,b,cov_matrix

def example():
    npts = 20
    m1 = 4.
    b1 = -10.
    sig1 = 1.
    x1 = np.linspace(-20.,20.,npts)
    m2 = 3.
    b2 = -20.
    sig2 = 1.
    x2 = np.linspace(30.,60.,npts)
    nTrials = 1000
    best_slope1 = np.zeros(nTrials)
    best_slope2 = np.zeros(nTrials)
    best_int1 = np.zeros(nTrials)
    best_int2 = np.zeros(nTrials)



    for i in range(nTrials):
        for j in range(nTrials):
            y1 = b1 + m1*x1 + np.random.randn(npts)*sig1
            y2 = b2 + m2*x2 + np.random.randn(npts)*sig2
        FIT1=FIT(x1,y1)
        FIT2=FIT(x2,y2)
        best_slope1[i]=FIT1[1]
        best_slope2[i]=FIT2[1]
        best_int1[i]=FIT1[0]
        best_int2[i]=FIT2[0]
        
    plt.plot(best_int1,best_slope1,".")
    plt.show()
    plt.plot(best_int2,best_slope2,".")
    plt.show()
example()
'''
#1. Collect your N-data points, 𝑥 and 𝑦 in numpy arrays

#2. Determine your data errors sigma_i for each of the y_i

#3. Write down your fitting model (here I assume K free parameters) in the form
    
#4. Construct the design matrix, M
#npts=1
#sigma=1
#M=np.zeros((npts,2))

#5. Construct the matrix 𝛼 = (M^T)*M
#Mt = M.transpose()
#alpha = np.dot(Mt,M)

#Check the size of alpha, it should be KxK where K is the number of free parameters.
#print(alpha.shape)

#6. Construct the inverse of alpha 𝛼^-1 = ((M^T)*M)^-1

#alpha_inverse=linalg.inv(alpha)

#Double check that the inverse worked out
#iden=np.dot(alpha_inverse)
#print(iden)

#7. Construct the vector yprime with elements yi/sigmai

#yprime=y/sigma

#8. The best fit parameters, p, are given by p=alpha^-1*M^T*yprime

#b=np.dot(Mt,yprime)
#p=np.dot(alpha_inverse,b)

#9. 
#for i in range(len(p)):
#   print(‘p[‘+str(i)+’]=‘+str(p[i])+’ +/- ‘+str(alpha_inverse[i,i]))

#10. Now plot out the residuals

#plt.clf()
#plt.errorbar(x,y-f(x,p),yerr=sigma,fmt='o')
#plt.xlabel(‘x-values’)
#plt.ylabel(‘Residuals’) '''
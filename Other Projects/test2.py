import numpy as np

a=np.array([[0,0,0]])
row_1=np.array([[1,2,3]])
a=np.append(a,row_1,axis=0)
print(a)
row_2=np.array([4,5,6])
a=np.append(a,[[row_2]],axis=1)
print(a)
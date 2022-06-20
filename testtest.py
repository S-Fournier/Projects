import numpy as np

x=np.array([0,1,2,3,4,5])

greet='hi'
goodbye='bye'
a=0

while a<5:
    
    print(x[a])

    if(x[a]<2):
        print(greet)
    else:
        print(goodbye)

    a=a+1
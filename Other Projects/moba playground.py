import numpy as np

#map N^2 dimension
map_N=10000
map_stuff=np.zeros(shape=(map_N,map_N))

def make_circle_unit(r,ID):
    n=r*2+1
    center=int(n/2)
    box=np.zeros(shape=(n,n))

    def circle(x,y,c,r):
        return (x-c)**2+(y-c)**2<=r**2
    for i in range(n):  
        for j in range(n):
            if(circle(i,j,center,r)==True):
                box[i,j]=ID
    return box

class minion:
    
    def __init__(self,type,x0,y0,ID):
        self.type=type
        self.x_position=x0
        self.y_position=y0
        if(type=='caster' or 'melee'):
            self.radius=50
        self.exist=make_circle_unit(self.radius,ID)
    def move(self,vx):
        self.x_position=self.x_position+vx
    def place(self,map):
        xplus=self.x_position+self.radius
        xminus=self.x_position-self.radius-1
        yplus=self.y_position+self.radius
        yminus=self.y_position-self.radius-1
        map[xminus:xplus,yminus:yplus]=map[xminus:xplus,yminus:yplus]+self.exist

minion_1=minion('melee',100,100,1)
minion_2=minion('melee',900,100,2)
minions=np.array([minion_1,minion_2])
minion_1.move(400)
minion_2.move(-400)
minion_1.place(map_stuff)
minion_2.place(map_stuff)
#IF MINION 1 DETECTS COLLISION, ID WILL POINT TO WHAT INDEX THE OTHER MINION IS AT
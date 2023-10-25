import numpy as np

Test_Grid=np.array([[0,1,2,3],[4,5,7,8],[9,10,11,12],[13,14,15,16]])

cell=2

for a in range(2):
    for b in range(2):
        Test_Bin=0
        for i in range(2):
            for j in range(2):
                print('a:',a,' b:',b,' i:',i,' j:',j)
                print(Test_Grid[cell*a+i][cell*b+j])
                Test_Bin=Test_Bin+Test_Grid[cell*a+i][cell*b+j]
        print('Sum of ',a,'',b,' quadrant:',Test_Bin)

#print(Test_Bin)
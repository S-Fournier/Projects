<<<<<<< Updated upstream
from turtle import shape
import numpy as np

test=np.array([[1,2,3],[4,5,6]])
test[0,:]=1
print(test)
=======
import numpy as np

class Player:
    def __init__(self,Left,Right):
        self.Left_Hand=Left
        self.Right_Hand=Right
        self.Records=np.array([])
    def Record(self,Round,Opponent_Left,Opponent_Right,Set_N,Option_N):
        np.append(self.Records,self.Left_Hand,self.Right_Hand,Opponent_Left,Opponent_Right,Set_N,Option_N)

Player_One=Player(1,1)
Player_Two=Player(1,1)

state=np.array(([Player_One.Left_Hand,Player_One.Right_Hand],[Player_Two.Left_Hand,Player_Two.Right_Hand]))

#DEFENDER GAINS ATTACKER'S FINGER COUNT
def attack(Attacker,Defender):
    Defender=Attacker+Defender
    if(Defender>=5):
        Defender=0
    return Defender

#DISTRIBUTE FINGER COUNT BETWEEN TWO HANDS
def distribute(Hand_A,Hand_B,N):
    Hand_A=Hand_A-N
    Hand_B=Hand_B+N
    return Hand_A,Hand_A

#USED TO SWITCH TURNS
def turn(i):
    N=i/2
    if (N<np.ceil(N)):
        return 'Player1'
    else:
        return 'Player2'

#CREATE SETS OF ACTIONS
def sets():
    set_one=['A(LL)','A(LR)','A(RL)','A(RR)','D(LR)','D(RL)']
    set_two=['A(RL)','A(RR)','D(LR)','D(RL)']
    set_three=['A(LL)','A(LR)','D(LR)','D(RL)']
    set_four=['A(LR)','A(RR)','D(LR)','D(RL)']
    set_five=['A(LL)','A(RL)','D(LR)','D(RL)']
    set_six=['A(LL)','A(LR)','A(RL)','A(RR)']
    return set_one,set_two,set_three,set_four,set_five,set_six

#PICK ONE OF THE SETS BASED ON CONDITIONS AND RANDOMLY CHOOSE AN ACTION FROM IT
def random_choice(Attacker_Left,Attacker_Right,Defender_Left,Defender_Right):
    if(Attacker_Left==0 and Defender_Left==0):
        option='A(RR)'
    elif(Attacker_Right==0 and Defender_Right==0):
        option='A(LL)'
    elif(Attacker_Left==0):
        option=np.random.choice(sets()[1])
    elif(Attacker_Right==0):
        option=np.random.choice(sets()[2])
    elif(Defender_Left==0):
        option=np.random.choice(sets()[3])
    elif(Defender_Right==0):
        option=np.random.choice(sets()[4])
    elif(Attacker_Left+Attacker_Right>=5):
        option=np.random.choice(sets()[5])
    else:
        option=np.random.choice(sets()[0])
    if(option=='D(LR)' and Attacker_Left==0):
        option='D(RL)'
    if(option=='D(RL)' and Attacker_Right==0):
        option='D(LR)'
    return option

#PERFORM THE ACTION
def move(Attacker_Left,Attacker_Right,Defender_Left,Defender_Right,option):
    state=np.array(([Attacker_Left,Attacker_Right],[Defender_Left,Defender_Right]))
    
    if(option=='A(RR)'):
        state[1,1]=attack(Attacker_Right,Defender_Right)
    elif(option=='A(RL)'):
        state[1,0]=attack(Attacker_Right,Defender_Left)
    elif(option=='A(LR)'):
        state[1,1]=attack(Attacker_Left,Defender_Right)
    elif(option=='A(LL)'):
        state[1,0]=attack(Attacker_Left,Defender_Left)
    elif(option=='D(LR)'):
        if(Attacker_Left==1):
            N=1
        else:
            N=np.random.randint(1,Attacker_Left+1)
        state[0,:]=distribute(Attacker_Left,Attacker_Right,N)
    elif(option=='D(RL)'):
        if(Attacker_Right==1):
            N=1
        else:
            N=np.random.randint(1,Attacker_Right+1)
        state[0,:]=distribute(Attacker_Right,Attacker_Left,N)   
    return state


i=1
z=100
while i<z:
    if(turn(i)=='Player1'):
        option=random_choice(*state[0,:],*state[1,:])
        state=move(*state[0,:],*state[1,:],option)
    elif(turn(i)=='Player2'):
        option=random_choice(*state[1,:],*state[0,:])
        state=move(*state[1,:],*state[0,:],option)
        state[[0,1]]=state[[1,0]]
    if(state[0,0]==0 and state[0,1]==0):
        print('Player1 is the winner')
        print('Won on turn',i)
        i=z
    if(state[1,0]==0 and state[1,1]==0):
        print('Player2 is the winner')
        print('Won on turn',i)
        i=z
    i=i+1
>>>>>>> Stashed changes

import numpy as np

class Player:
  def __init__(self,Left_Hand,Right_Hand):
    self.Left=Left_Hand_Hand
    self.Right=Right_Hand
    self.Records=np.array([])
  def Record(Turn_N,Opponent_Left,Opponent_Right,Set_N,Option_N):
    Temp_Record=np.array([Turn_N,self.Left,self.Right,Opponent_Left,Opponent_Right,Set_N,Option_N])
    if(np.size(self.Records)==0):
      self.Records=np.insert(self.Records,0,Temp_Record)
    else:
      self.Records=np.vstack((self.Records,Temp_Record))

Player_One=Player(1,1)
Player_Two=Player(1,1)

P1R=1
P1L=1

P2R=1
P2L=1

state=np.array(([P1L,P1R],[P2L,P2R]))

set_one=['A(LL)','A(LR)','A(RL)','A(RR)','D(LR)','D(RL)']
set_two=['A(RL)','A(RR)','D(LR)','D(RL)']
set_three=['A(LL)','A(LR)','D(LR)','D(RL)']
set_four=['A(LR)','A(RR)','D(LR)','D(RL)']
set_five=['A(LL)','A(RL)','D(LR)','D(RL)']
set_six=['A(LL)','A(LR)','A(RL)','A(RR)']

def attack(a,b):
    b=a+b
    if(b>=5):
        b=0
    return b

def distribute(a,b,N):
    a=a-N
    b=b+N
    return a,b

def turn(i):
    q=i/2
    if(q<np.ceil(q)):
        return 'Player1'
    else:
        return 'Player2'

#P=PLAYER, A=ATTACKER, D=DEFENDER R=RIGHT, L= LEFT
def move(Attacker_Left,Attacker_Right,Defender_Left,Defender_Right):
    state=np.array(([Attacker_Left,Attacker_Right],[Defender_Left,Defender_Right]))
    if(Attacker_Left==0 and Defender_Left==0):
        option='A(RR)'
    elif(Attacker_Right==0 and Defender_Right==0):
        option='A(LL)'
    elif(Attacker_Left==0):
        option=np.random.choice(set_two)
    elif(Attacker_Right==0):
        option=np.random.choice(set_three)
    elif(Defender_Left==0):
        option=np.random.choice(set_four)
    elif(Defender_Right==0):
        option=np.random.choice(set_five)
    elif(Attacker_Left+Attacker_Right>=5):
        option=np.random.choice(set_six)
    else:
        option=np.random.choice(set_one)
    
    if(option=='D(LR)' and Attacker_Left==0):
        option='D(RL)'
    if(option=='D(RL)' and Attacker_Right==0):
        option='D(LR)'
    print('option',option)
    

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
    print(turn(i))
    if(turn(i)=='Player1'):
        state=move(*state[0,:],*state[1,:])
    elif(turn(i)=='Player2'):
        state=move(*state[1,:],*state[0,:])
        state[[0,1]]=state[[1,0]]
    print(state)
    print('')
    if(state[0,0]==0 and state[0,1]==0):
        print('Player1 is the winner')
        print('Won on turn',i)
        i=z
    if(state[1,0]==0 and state[1,1]==0):
        print('Player2 is the winner')
        print('Won on turn',i)
        i=z
    i=i+1

#NEW GOAL: ADD A PROBABILITY DISTRIBUTION FOR EACH PLAYER AND INCREASE PROBABILITY FOR WINNING MOVE AND DECREASE FOR LOWING MOVE

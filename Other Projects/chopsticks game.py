import numpy as np

Initial_P_Set=np.ones((8,6))
Initial_P_Set[1:,4:]=0
Initial_P_Set[6:,2:]=0
Initial_P_Set[0,:]=1/6
Initial_P_Set[1:6]=Initial_P_Set[1:6]*1/4
Initial_P_Set[6:]=Initial_P_Set[6:]*1/2
class Player:
    def __init__(self,Left_Hand,Right_Hand,Initial_P_Set):
        self.Left=Left_Hand
        self.Right=Right_Hand
        self.Records=np.array([])
        self.testing=np.ones((8,6))
        self.P_Set=Initial_P_Set
        self.Set_One=['A(LL)','A(LR)','A(RL)','A(RR)','D(LR)','D(RL)']
        self.Set_Two=['A(RL)','A(RR)','D(LR)','D(RL)','','']
        self.Set_Three=['A(LL)','A(LR)','D(LR)','D(RL)','','']
        self.Set_Four=['A(LR)','A(RR)','D(LR)','D(RL)','','']
        self.Set_Five=['A(LL)','A(RL)','D(LR)','D(RL)','','']
        self.Set_Six=['A(LL)','A(LR)','A(RL)','A(RR)','','']
        self.Set_Seven=['A(LL)','D(LR)','','','','']
        self.Set_Eight=['A(RR)','D(RL)','','','','']
    def Record(self,Turn_N,Opponent_Left,Opponent_Right,Set_N,Option_N):
        Temp_Record=np.array([Turn_N,self.Left,self.Right,Opponent_Left,Opponent_Right,Set_N,Option_N])
        if(np.size(self.Records)==0):
            self.Records=np.insert(self.Records,0,Temp_Record)
        else:
            self.Records=np.vstack((self.Records,Temp_Record))

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

def option_select(Attacker_Left,Attacker_Right,Defender_Left,Defender_Right,Player):
    temp_P_Set=Player.P_Set
    if(Attacker_Left==0 and Defender_Left==0):
        option=np.random.choice(Player.Set_Eight,p=temp_P_Set[7,:])
        set_N=8
    elif(Attacker_Right==0 and Defender_Right==0):
        option=np.random.choice(Player.Set_Seven,p=temp_P_Set[6,:])
        set_N=7
    elif(Attacker_Left==0):
        option=np.random.choice(Player.Set_Two,p=temp_P_Set[1,:])
        set_N=2
    elif(Attacker_Right==0):
        option=np.random.choice(Player.Set_Three,p=temp_P_Set[2,:])
        set_N=3
    elif(Defender_Left==0):
        option=np.random.choice(Player.Set_Four,p=temp_P_Set[3,:])
        set_N=4
    elif(Defender_Right==0):
        option=np.random.choice(Player.Set_Five,p=temp_P_Set[4,:])
        set_N=5
    elif(Attacker_Left+Attacker_Right>=5):
        option=np.random.choice(Player.Set_Six,p=temp_P_Set[5,:])
        set_N=6
    else:
        option=np.random.choice(Player.Set_One,p=temp_P_Set[0,:])
        set_N=1
    if(option=='D(LR)' and Attacker_Left==0):
        option='D(RL)'
    if(option=='D(RL)' and Attacker_Right==0):
        option='D(LR)'
    return option,set_N
  
def option_conversion(option):
    set=np.array(['A(LL)','A(LR)','A(RL)','A(RR)','D(LR)','D(RL)'])
    option_N=np.array([100,101,110,111,1,10])
    option_index=np.where(set==option)
    option_N=np.int(option_N[option_index])
    return option_N

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

def prob_adjustment(Set_N,Option_N,turn,set_P):
    if(Set_N==1):
        set=np.array([100,101,110,111,1,10])
    elif(Set_N==2):
        set=np.array([110,111,1,10])
    elif(Set_N==3):
        set=np.array([100,101,1,10])
    elif(Set_N==4):
        set=np.array([101,111,1,10])
    elif(Set_N==5):
        set=np.array([100,110,1,10])
    elif(Set_N==6):
        set=np.array([100,101,110,111])
    elif(Set_N==7):
        set=np.array([100,1])
    elif(Set_N==8):
        set=np.array([111,10])

    set_index=np.where(set==Option_N)

    if(turn==1):
        set_P[set_index]=2*set_P[set_index]
        normalizer=1/(np.sum(set_P))
        set_P=set_P*normalizer
    
    if(turn==2):
        set_P[set_index]=3*set_P[set_index]
        normalizer=(len(set))/(np.sum(set_P))
        set_P=set_P*normalizer
    
    return set_P

for a in range(100):

    Player_One=Player(1,1,Initial_P_Set)
    Player_Two=Player(1,1,Initial_P_Set)

    state=np.array(([Player_One.Left,Player_One.Right],[Player_Two.Left,Player_Two.Right]))



    i=1
    z=100

    while i<z:

        if(turn(i)=='Player1'):
            option_n_set=option_select(*state[0,:],*state[1,:],Player_One)
            option=option_n_set[0]
            set_N=option_n_set[1]
            option_N=option_conversion(option)
            state=move(*state[0,:],*state[1,:],option)
            Player_One.Left=state[0,0]
            Player_One.Right=state[0,1]
            Player_One.Record(i,*state[1,:],set_N,option_N)
        elif(turn(i)=='Player2'):
            option_n_set=option_select(*state[1,:],*state[0,:],Player_Two)
            option=option_n_set[0]
            set_N=option_n_set[1]
            option_N=option_conversion(option)
            state=move(*state[1,:],*state[0,:],option)
            Player_Two.Left=state[0,0]
            Player_Two.Right=state[0,1]
            Player_Two.Record(i,*state[1,:],set_N,option_N)
            state[[0,1]]=state[[1,0]]
            
        if(state[0,0]==0 and state[0,1]==0):
            Player_One.P_Set[set_N-1,:]=prob_adjustment(set_N,option_N,1,Player_One.P_Set[set_N-1,:])
            print('Player1 is the winner')
            print('Won on turn',i)
            i=z
        if(state[1,0]==0 and state[1,1]==0):
            print('Player2 is the winner')
            print('Won on turn',i)
            Player_Two.P_Set[set_N-1,:]=prob_adjustment(set_N,option_N,1,Player_Two.P_Set[set_N-1,:])
            i=z
        i=i+1
    print(Player_One.Records)
    print(Player_Two.Records)
import numpy as np

class Hand:

    def __init__(self,Fingers):
        self.Fingers=Fingers
        self.Options=np.array(['Attack Left','Attack Right'])
        self.Available=True
        self.P=1
    def Check(self):
        if(self.Fingers==5):
            self.Fingers=0
        if(self.Fingers==0):
            self.Available=False
            self.P=0
        elif(self.Fingers==1):
            self.Options=np.array(['Attack Left','Attack Right'])
        elif(self.Fingers>1 and self.Fingers<5):
            self.Options=np.array(['Attack Left','Attack Right','Distribute'])
        else:
            print('Error')
    def Flip(self):
        Result=np.random.uniform(0,1)*self.P
        return Result

def attack(Attacker,Defender):
    Defender=Attacker+Defender
    if(Defender>=5):
        Defender=0
    return Defender

def distribute(Active_Hand,Other_Hand,N):
    Active_Hand=Active_Hand-N
    Other_Hand=Other_Hand+N
    return Active_Hand,Other_Hand

def turn(Turn_N):
    N=Turn_N/2
    if(N<np.ceil(N)):
        return 'Player1'
    else:
        return 'Player2'

def option_select(Active_Hand,Opponent,Other_hand):
    temp=np.array([0,0])
    for i in range(len(Opponent)):
        temp[i]=Opponent[i].Available
    if(Other_hand.Fingers>1):
        Opponent=np.append(Opponent,Other_hand.Available)
    indexes=np.where(temp==True)
    option=np.random.choice(Active_Hand.Options[indexes])
    if(option=='Attack Left'):
        Opponent[0].Fingers=attack(Active_Hand.Fingers,Opponent[0].Fingers)
    elif(option=='Attack Right'):
        Opponent[1].Fingers=attack(Active_Hand.Fingers,Opponent[1].Fingers)
    elif(option=='Distribute'):
        Opponent[2].Fingers=distribute(Active_Hand.Fingers,Opponent[2].Fingers,np.random.randint(1,Active_Hand.Fingers-1))
    else:
        print('Error')
    return Active_Hand,Opponent,Other_hand

class Game:
    def __init__(self,Player1,Player2):
        self.Player1=Player1
        self.Player2=Player2
        self.Set=np.append(Player1,Player2)
    
P1L=Hand(1)
P1R=Hand(1)
P2L=Hand(1)
P2R=Hand(1)

Player1=np.array([P1L,P1R])
Player2=np.array([P2L,P2R])

Player1_Check=np.array([P1L.Available,P1R.Available])
Player2_Check=np.array([P2L.Available,P2R.Available])

Game_Set=np.append(Player1,Player2)
Game_Set_Temp=np.array([1,1,1,1])
Game_Check=np.append(Player1_Check,Player2_Check)
Game_Records=np.array([1,1,1,1])

Turn_N=1
Game=True

while Game==True:

    if(turn(Turn_N)=='Player1'):
        if(P1L.Flip()>P1R.Flip()):
            option_select(P1L,Player2,P1R)
        else:
            option_select(P1R,Player2,P1R)

    elif(turn(Turn_N)=='Player2'):
        if(P2L.Flip()>P2R.Flip()):
            option_select(P2L,Player1,P2R)
        else:
            option_select(P2R,Player1,P2R)

    for i in range(len(Game_Set)):
        Game_Set[i].Check()
        Game_Check[i]=Game_Set[i].Available
        Game_Set_Temp[i]=Game_Set[i].Fingers
    Game_Records=np.vstack((Game_Records,Game_Set_Temp))
    
    if(Game_Check[0]==False and Game_Check[1]==False):
        print('Player2 is the winner on turn',Turn_N)
        Game_Records=np.vstack((Game_Records,[9,9,9,9]))
        Game=False
    elif(Game_Check[2]==False and Game_Check[3]==False):
        print('Player1 is the winner on turn',Turn_N)
        Game_Records=np.vstack((Game_Records,[9,9,9,9]))
        Game=False
    
    Turn_N=Turn_N+1

print(Game_Records)
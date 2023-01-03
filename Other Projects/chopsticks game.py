import numpy as np
import csv

#CREATED A PLAYER CLASS THAT WILL HOLD ALL OPTION AND PROBABILITY SET ALONG WITH THEIR
#OWN RECORDS OF TURNS
#ADDITIONALY, EACH PLAYER WILL STORE THE NUMBER OF FINGERS OF EACH HAND
#THIS IS VERY ESSENTIAL TO THE GAME
class Player:
    def __init__(self,Left_Hand,Right_Hand,Initial_P_Set):
        
        self.Left=Left_Hand
        self.Right=Right_Hand
        self.Records=np.array([]) #WHERE EVERYTHING IS STORED
        self.P_Set=Initial_P_Set

        #SETS USED TO RANDOMLY DETERMINE OPTION
        #A=ATTACK, D=DISTRIBUTE LL=LEFT TO LEFT, RR= RIGHT TO RIGHT,... ETC.
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


#THE ATTACK AND DISTRIBUTE FUNCTION
#THE GOAL IS TO GET BOTH ENEMY PLAYER HANDS TO 5->0
#DISTRIBUTING IS USED TO SPREAD OUT YOUR FINGERS IN ORDER TO MINIMIZE DAMAGE

def attack(Attacker,Defender):
    Defender=Attacker+Defender
    if(Defender>=5):
        Defender=0
    return Defender

def distribute(Hand_One,Hand_Two,N):
    Hand_One=Hand_One-N
    Hand_Two=Hand_Two+N
    return Hand_One,Hand_Two

#A WAY FOR THE PLAYERS TO TAKE TURNS
def turn(Turn_N):
    N=Turn_N/2
    if(N<np.ceil(N)):
        return 'Player1'
    else:
        return 'Player2'

<<<<<<< Updated upstream
#CHOOSE A RANDOM MOVE OPTION BASED ON STATE OF THE GAME
def option_select(Attacker_Left,Attacker_Right,Defender_Left,Defender_Right,Player):
    
    #TEMPORARY VARIABLE TO STORE THE PROBABILITY SETS
    Temp_P_Set=Player.P_Set
    
    #IF/ELIF/ELSE STATEMENTS THAT LOOKS THROUGH ALL POSSIBLE STATES
    #USES CORRELATED PROBABILITY SET TO CHOOSE AN OPTION
=======
def move(Attacker_Left,Attacker_Right,Defender_Left,Defender_Right):
    state=np.array(([Attacker_Left,Attacker_Right],[Defender_Left,Defender_Right]))
>>>>>>> Stashed changes
    if(Attacker_Left==0 and Defender_Left==0):
        option=np.random.choice(Player.Set_Eight,p=Temp_P_Set[7,:])
        set_N=8
    elif(Attacker_Right==0 and Defender_Right==0):
        option=np.random.choice(Player.Set_Seven,p=Temp_P_Set[6,:])
        set_N=7
    elif(Attacker_Left==0):
        option=np.random.choice(Player.Set_Two,p=Temp_P_Set[1,:])
        set_N=2
    elif(Attacker_Right==0):
        option=np.random.choice(Player.Set_Three,p=Temp_P_Set[2,:])
        set_N=3
    elif(Defender_Left==0):
        option=np.random.choice(Player.Set_Four,p=Temp_P_Set[3,:])
        set_N=4
    elif(Defender_Right==0):
        option=np.random.choice(Player.Set_Five,p=Temp_P_Set[4,:])
        set_N=5
    elif(Attacker_Left+Attacker_Right>=5):
        option=np.random.choice(Player.Set_Six,p=Temp_P_Set[5,:])
        set_N=6
    else:
        option=np.random.choice(Player.Set_One,p=Temp_P_Set[0,:])
        set_N=1
    
    #CHECKS TO MAKE SURE THAT THE PLAYER IS NOT DISTRIBUTING WITH NO FINGERS
    if(option==1 and Attacker_Left==0):
        option=10
    if(option==10 and Attacker_Right==0):
        option=1
    
<<<<<<< Updated upstream
    return option,set_N

#CONVERTS OPTION STRING TO A BINARY VALUE
def option_conversion(option):
    set=np.array(['A(LL)','A(LR)','A(RL)','A(RR)','D(LR)','D(RL)'])
    option_N=np.array([100,101,110,111,1,10])
    option_index=np.where(set==option)
    option_N=int(option_N[option_index])
    return option_N

#TAKES OPTION AND PERFORMS THE ASSOCIATED MOVE
def move(Attacker_Left,Attacker_Right,Defender_Left,Defender_Right,option):
    Game_State=np.array(([Attacker_Left,Attacker_Right],[Defender_Left,Defender_Right]))
    
=======
>>>>>>> Stashed changes
    if(option=='A(RR)'):
        Game_State[1,1]=attack(Attacker_Right,Defender_Right)
    elif(option=='A(RL)'):
        Game_State[1,0]=attack(Attacker_Right,Defender_Left)
    elif(option=='A(LR)'):
        Game_State[1,1]=attack(Attacker_Left,Defender_Right)
    elif(option=='A(LL)'):
        Game_State[1,0]=attack(Attacker_Left,Defender_Left)

    #DISTRIBUTE A RANDOM AMOUNT BETWEEN 1 AND THE MAX AMOUNT OF FINGERS IN HAND
    elif(option=='D(LR)'):
        if(Attacker_Left==1):
            N=1
        else:
            print(Attacker_Left)
            N=np.random.randint(1,Attacker_Left-1)
        Game_State[0,:]=distribute(Attacker_Left,Attacker_Right,N)
    elif(option=='D(RL)'):
        if(Attacker_Right==1):
            N=1
        else:
            print(Attacker_Right)
            N=np.random.randint(1,Attacker_Right-1)
        Game_State[0,:]=distribute(Attacker_Right,Attacker_Left,N)   
    return Game_State

#WHEN A PLAYER WINS, TAKE THEIR PROBABILITY SET AND INCREASE THE LIKELYHOOD THAT THEY
#WILL DO THE LAST MOVE
def prob_adjustment(Set_N,Option_N,turn,Set_P):
    if(Set_N==1):
        Set=np.array([100,101,110,111,1,10])
    elif(Set_N==2):
        Set=np.array([110,111,1,10])
    elif(Set_N==3):
        Set=np.array([100,101,1,10])
    elif(Set_N==4):
        Set=np.array([101,111,1,10])
    elif(Set_N==5):
        Set=np.array([100,110,1,10])
    elif(Set_N==6):
        Set=np.array([100,101,110,111])
    elif(Set_N==7):
        Set=np.array([100,1])
    elif(Set_N==8):
        Set=np.array([111,10])

    set_index=np.where(set==Option_N)

    #HAVE TO NORMALIZE DISTRIBUTION AFTER EVERY CHANGE

    if(turn==1):
        Set_P[set_index]=2*Set_P[set_index]
        normalizer=1/(np.sum(Set_P))
        Set_P=Set_P*normalizer
    
    if(turn==2):
        Set_P[set_index]=3*Set_P[set_index]
        normalizer=(len(set))/(np.sum(Set_P))
        Set_P=Set_P*normalizer
    
    return Set_P

#PUTTING EVERYTHING TOGETHER
#CURRENTLY SETUP TO DO 100 GAMES

#INITIALIZING A MATRIX OF PROBABILITY DISTRIBUTIONS FOR EACH SET
#HAD TO MAKE IT A MAXTRIX FOR CLEANILNESS, BUT HAD TO DO IT OUTSIDE THE CLASS
#WILL STORE IN CLASS
Initial_P_Set=np.ones((8,6))
Initial_P_Set[1:,4:]=0
Initial_P_Set[6:,2:]=0
Initial_P_Set[0,:]=1/6
Initial_P_Set[1:6]=Initial_P_Set[1:6]*1/4
Initial_P_Set[6:]=Initial_P_Set[6:]*1/2

Rounds=20
Games=1000
Game_Records=np.zeros(shape=(Rounds,8,Games))

Player_One=Player(1,1,Initial_P_Set)
Player_Two=Player(1,1,Initial_P_Set)

for a in range(100):

    #RESET EACH HAND TO 1 FINGER
    Player_One.Left=1
    Player_One.Right=1
    Player_Two.Left=1
    Player_Two.Right=1

    Game_State=np.array(([Player_One.Left,Player_One.Right],[Player_Two.Left,Player_Two.Right]))

    i=1

    while i<Rounds:

        if(turn(i)=='Player1'):
            option_n_set=option_select(*Game_State[0,:],*Game_State[1,:],Player_One)
            option=option_n_set[0]
            set_N=option_n_set[1]
            option_N=option_conversion(option)
            Game_State=move(*Game_State[0,:],*Game_State[1,:],option)
            Player_One.Left=Game_State[0,0]
            Player_One.Right=Game_State[0,1]
            Player_One.Record(i,*Game_State[1,:],set_N,option_N)
            Game_Records[i-1,:7,a]=np.array([i,*Game_State[0,:],*Game_State[1,:],set_N,option_N])
            
        elif(turn(i)=='Player2'):
            option_n_set=option_select(*Game_State[1,:],*Game_State[0,:],Player_Two)
            option=option_n_set[0]
            set_N=option_n_set[1]
            option_N=option_conversion(option)
            Game_State=move(*Game_State[1,:],*Game_State[0,:],option)
            Player_Two.Left=Game_State[0,0]
            Player_Two.Right=Game_State[0,1]
            Player_Two.Record(i,*Game_State[1,:],set_N,option_N)
            Game_State[[0,1]]=Game_State[[1,0]]
            Game_Records[i-1,:7,a]=np.array([i,*Game_State[0,:],*Game_State[1,:],set_N,option_N])
            
        if(Game_State[0,0]==0 and Game_State[0,1]==0):
            print('Player1 is the winner')
            print('Won on turn',i)
            Game_Records[:i,7,a]=1
            #Player_One.P_Set[set_N-1,:]=prob_adjustment(set_N,option_N,1,Player_One.P_Set[set_N-1,:])
            i=Rounds
        if(Game_State[1,0]==0 and Game_State[1,1]==0):
            print('Player2 is the winner')
            print('Won on turn',i)
            Game_Records[:i,7,a]=2
            #Player_Two.P_Set[set_N-1,:]=prob_adjustment(set_N,option_N,1,Player_Two.P_Set[set_N-1,:])
            i=Rounds
        i=i+1

with open('chop.csv', 'w', encoding='UTF8', newline='') as file:
    writer=csv.writer(file)
    for x in range(Games):
        writer.writerows(Game_Records[:,:,x])
    file.close()
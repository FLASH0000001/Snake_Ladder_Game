import tkinter as tk
from PIL import ImageTk,Image
import random
from gtts import gTTS
from playsound import playsound
import os

def Speak(Text):
    
    obj = gTTS(text= Text,lang= 'en',slow =False)
    obj.save('Text.mp3')
    playsound('Text.mp3')
    os.remove('Text.mp3')

def start_game():
    global im
    global b1,b2

    # Buttons for Players
    # Player -1
    b1.place(x=1200,y=400)
    # Player -2
    b2.place(x=1200,y=600)

    # Dice
    im = Image.open("PHOTOS/roll.png")
    im = im.resize((65,65))
    im = ImageTk.PhotoImage(im)
    b3 = tk.Button(root,image=im,height=80,width=80,bg="black",activebackground='yellow')
    b3.place(x=1275,y=200)

    # Exit Button
    b4 = tk.Button(root,text="Click Here to Exit!",height=3,width=20,fg="white",bg="black",font=('Cursive',14,'bold'),activebackground='grey',command=root.destroy)
    b4.place(x=1200,y=20)

def reset_coins():
    global player_1,player_2
    global pos1,pos2
    
    player_1.place(x=0,y=725)
    player_2.place(x=50,y=725)

    pos1=0
    pos2=0

def load_dice_images():
    global Dice
    names=["1.png","2.png","3.png","4.png","5.png","6.png"]
    for nam in names:
        im = Image.open("PHOTOS/"+nam)
        im = im.resize((65,65))
        im = ImageTk.PhotoImage(im)
        Dice.append(im)

def check_Ladder(Turn):
    global pos1,pos2
    global Ladder

    f=0 # No Ladder
    if Turn==1:
        if pos1 in Ladder:
            Speak("Ladder at "+str(pos1)+" Moving up to "+str(Ladder[pos1]))
            pos1 = Ladder[pos1]
            f=1
    else:
        if pos2 in Ladder:
            Speak("Ladder at "+str(pos2)+" Moving up to "+str(Ladder[pos2]))
            pos2 = Ladder[pos2]
            f=1
    return f

def check_Snake(Turn):
    global pos1,pos2
    global Snake

    if Turn==1:
        if pos1 in Snake:
            Speak("Snake head at "+str(pos1)+" Going down to "+str(Snake[pos1]))
            pos1 = Snake[pos1]
    else:
        if pos2 in Snake:
            Speak("Snake head at "+str(pos2)+" Going down to "+str(Snake[pos2]))
            pos2 = Snake[pos2]
    

def roll_dice():
    global Dice
    global turn
    global pos1,pos2
    global b1,b2

    r = random.randint(1,6)
    b5 = tk.Button(root,image=Dice[r-1],height=80,width=80,bg="black",activebackground='yellow')
    b5.place(x=1275,y=200)

    Speak(str(r))

    Lad=0   # No Ladder
    if turn==1:
        if (pos1+r)<=100:
            pos1 = pos1 + r
        Lad=check_Ladder(turn)
        check_Snake(turn)
        move_coin(turn,pos1)
        if r!=6 and Lad!=1:
            turn=2
            b1.configure(state='disabled')
            b2.configure(state='normal')
    else:
        if (pos2+r)<=100:
            pos2 = pos2 + r
        Lad=check_Ladder(turn)
        check_Snake(turn)
        move_coin(turn,pos2)
        if r!=6 and Lad!=1:
            turn=1
            b1.configure(state='normal')
            b2.configure(state='disabled')
    Speak("Player - "+str(turn)+ " turn ")

    is_winner()

def is_winner():
    global pos1,pos2

    if pos1==100:
        msg1="Player - 1 is the Winner"
        Speak(msg1)
        Lab = tk.Label(root,text=msg1,height=2,width=20,fg='red',bg='white',font=('Cursive',30,'bold'))
        Lab.place(x=300,y=300)
        reset_coins()
    elif pos2==100:
        msg2="Player - 2 is the Winner"
        Speak(msg2)
        Lab = tk.Label(root,text=msg2,height=2,width=20,fg='blue',bg='white',font=('Cursive',30,'bold'))
        Lab.place(x=300,y=300)
        reset_coins()
        
def move_coin(Turn,r):
    global player_1,player_2
    global Index,pos1,pos2

    if Turn==1:
        player_1.place(x=Index[r][0],y=Index[r][1])
        Speak("You are at "+str(pos1))

    else:
        player_2.place(x=Index[r][0],y=Index[r][1])
        Speak("You are at "+str(pos2))

def get_Index():
    global player_1,player_2
    
    Num=[100,99,98,97,96,95,94,93,92,91,81,82,83,84,85,86,87,88,89,90,80,79,78,77,76,75,74,73,72,71,61,62,63,64,65,66,67,68,69,70,60,59,58,57,56,55,54,53,52,51,41,42,43,44,45,46,47,48,49,50,40,39,38,37,36,35,34,33,32,31,21,22,23,24,25,26,27,28,29,30,20,19,18,17,16,15,14,13,12,11,1,2,3,4,5,6,7,8,9,10]
    row=15
    i=0
    for x in range(1,11):
        col=30
        for y in range(1,11):
            Index[Num[i]]=(col,row)
            col = col + 100
            i= i+1
        row = row + 70
    print(Index)
       
# To Store Dice Images
Dice=[]

# To store x & y Co-ordinates of given Num
Index={}

# Initial Positions of Players
pos1=None
pos2=None

# Ladder Bottom to Top
Ladder={2:23,6:45,20:59,52:72,57:96,71:92}

# Snake Head to Tail
Snake={98:40,87:49,84:58,73:15,56:8,50:5,43:17}

root = tk.Tk()
root.geometry("1200x800")
root.title("Snake and Ladder Game")

F1= tk.Frame(root,width=1200,height=800,relief='raised')
F1.place(x=0,y=0)

# Set Board
img1 = ImageTk.PhotoImage(Image.open("PHOTOS/cover.png"))
Lab = tk.Label(F1,image=img1)
Lab.place(x=0,y=0)

# Player -1 Button
b1 = tk.Button(root,text="Player - 1",height=3,width=20,fg="white",bg="red",font=('Cursive',14,'bold'),activebackground='purple',command=roll_dice)
    
# Player -2 Button
b2 = tk.Button(root,text="Player - 2",height=3,width=20,fg="white",bg="blue",font=('Cursive',14,'bold'),activebackground='green',command=roll_dice)
    
# Player 1 coin
player_1 = tk.Canvas(root,width=40,height=40)
player_1.create_oval(10,10,40,40,fill='red')

# Player 2 coin
player_2 = tk.Canvas(root,width=40,height=40)
player_2.create_oval(10,10,40,40,fill='blue')

# Whose turn First...by default Player -1
turn = 1

# Keep coins at Initial Positions
reset_coins()

# Get Index of Each Num
get_Index()

# Load Dice Images
load_dice_images()

Speak("Welcome to Snake and Ladder Game.....Start the game With Player - 1")
# Setting All the Buttons
start_game()

root.mainloop()

import random
from tkinter import Tk, Label, Button, PhotoImage
from tkinter.messagebox import *
import sys

page = Tk()
page.title('Rock-Paper-Scissors')
scores = [0,'-',0]
winners = ['RockScissors','PaperRock','ScissorsPaper']
option = ('Rock', 'Paper', 'Scissors')

rock_img = PhotoImage(file='assets/rock.png')
paper_img = PhotoImage(file='assets/paper.png')
scissors_img = PhotoImage(file='assets/scissors.png')
play_img = PhotoImage(file='assets/play.png')
quit_img = PhotoImage(file='assets/quit.png')

def choose(item):
	output.config(text ='')
	output['text'] = item

def end():
	sys.exit()
	
def play():
	com = random.choice(option)
	sub = output.cget('text')
	
	if com == sub:
		output.config(text ='')
		output['text'] = 'Draw!\nComputer Choose '+com
	elif sub + com in winners:
		scores[0]+=1
		if scores[0]==10:
		    showinfo('Rock-Paper-Scissors', 'Congratulation!!!\nYou Won The Match')
		    end()
		output.config(text ='')
		output['text'] = 'You Win!\nComputer Choose '+com
	else:
		scores[2]+=1
		if scores[2]==10:
		    showerror('Rock-Paper-Scissors', 'Oh No!!!\nYou Lost The Match')
		    end()
		output.config(text ='')
		output['text'] = 'You Lose!\nComputer Choose '+com
	Label(page, text=scores, font=('arial',7,'bold')).grid(row=1, column=1)
	
showinfo('Rock-Paper-Scissors', 'TASK:\nReach 10 Points First', icon='question')
	
Label(page, text='Player', font=('arial',7,'bold')).grid(row=1, column=0)
Label(page, text='Computer', font=('arial',7,'bold')).grid(row=1, column=2)

output = Label(page, height=3, fg='navy', font=('times new roman',8,'bold'))
output.grid(row=2, columnspan=3)
	
Button(page, image=rock_img, borderwidth=0, command=lambda:choose('Rock')).grid(row=3, column=0)
Button(page, image=paper_img, borderwidth=0, command=lambda:choose('Paper')).grid(row=3, column=1)
Button(page, image=scissors_img, borderwidth=0, command=lambda:choose('Scissors')).grid(row=3, column=2)
Button(page, image=play_img, borderwidth=0, command=play).grid(row=4, columnspan=2, ipadx=80)
Button(page, image=quit_img, borderwidth=0,command=end).grid(row=4, column=2)

page.mainloop()
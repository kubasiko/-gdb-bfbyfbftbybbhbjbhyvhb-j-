'''
import tkinter
import random
from tkinter import PhotoImage

def prepare_and_start():
    global player
    canvas.delete('all')
    player_pos=(random.randint(1,N_X-1)*step,random.randint(1,N_Y-1)*step)
    player=canvas.create_image((player_pos[0],player_pos[1]),image=player_pic,anchor='nw')
    master.bind('<KeyPress>',key_pressed)
    
def move_wrap(obj,move_x,move_y):
    xy=canvas.coords(obj)
    canvas.move(obj,move_x,move_y)
    print(xy)
    if xy[0]<=0:
        canvas.move(obj,WIDTH,0)  
    if xy[0]>=0:
        canvas.move(obj,-WIDTH,0)
    if xy[1]<=0:
        canvas.move(obj,0,HEIGHT)  
    if xy[1]>=0:
        canvas.move(obj,0,-HEIGHT)
         
def key_pressed(event):
    if event.keysym=='Up':
        move_wrap(player,0,-step)
    if event.keysym=='Down':
        move_wrap(player,0,step)
    if event.keysym=='Right':
        move_wrap(player,step,0)
    if event.keysym=='Left':
        move_wrap(player,-step,0)          

master=tkinter.Tk()
step=32
N_X=20
N_Y=20
WIDTH= step*N_X
HEIGHT=step*N_Y
player_pic=tkinter.PhotoImage(file=r"курочка баязитов.png")
restart=tkinter.Button(text='начать заново')

canvas=tkinter.Canvas(bg='blue', width=WIDTH,height=HEIGHT)
label=tkinter.Label(text='найди выход')
restart=tkinter.Button(master,text='restart',command=prepare_and_start)
restart.pack()
label.pack()
canvas.pack()
prepare_and_start()
master.bind('<KeyPress>',key_pressed)
tkinter.mainloop()
'''
'''
import pygame
pygame.init()
win=pygame.display.set_mode((500,500))
color=(54,54,54)
win.fill(color)
pygame.display.update()
win.fill((255,255,255))
pygame.draw.circle(win, (48,255,0),(250,240),50)
pygame.draw.circle(win, (255,24,27),(250,30),50)
pygame.draw.circle(win, (235,255,0),(250,130),50)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
'''
'''
import pygame
pygame.init()
win=pygame.display.set_mode((500,500))
win.fill((255,255,255))
pygame.draw.line(win,(0,255,255),(0,0),(100,100),5)
pygame.draw.lines(win,(0,0,0),True,((200,200),(300,300),(300,250)),10)
#pygame.draw.polygon(win,(0,0,0),[(0,100),(100,50),(100,150)],False)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
'''
'''
import pygame
def create_crossed_lines(width,height):
    win=pygame.display.set_mode((width,height))
    win.fill((0,0,0))
    pygame.draw.line(win,(255,255,255),(0,0),(width,height),5)
    pygame.draw.line(win,(255,255,255),(0,height),(height,0),5)
    pygame.display.update()
pygame.init()
def get_integer_input():
    while True:
        input_data=input('fdgbdf gf g')
        data=input_data.split()
        if len(data)==2 and data[0].isdigit and data[1].isdigit():
            width=int(data[0])
            height=int(data[1])
            return width,height
        else:
            print('щшибка палораплдшнткмапрц')
width,height=get_integer_input()
create_crossed_lines(width,height)
            

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
'''
'''
import pygame
pygame.init()
str=input('числа введи 2 через проабел')
list=str.split()
a=int(list[0])
bul=int(list[1])
win = pygame.display.set_mode(a, a)
pygame.display.set_caption('chess board')


cell_size=str//bul
white=(255,255,255)
black=(0,0,0)
for i in range(bul):
    for j in range(bul):
        if(i+j)%2==0:
            color=black
        else:
            pygame.draw.rect(win,color,(j*cell_size),(bul-1-i)*cell_size,cell_size,cell_size)
            pygame.display.flip()
            

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
'''

import pygame
pygame.init()
win=pygame.display.set_mode((700,500))
x=101
dir=1
dir_1=1
der=1
der_1=1
y=50
x_1=325
y_2=275
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    if dir==1:
        x+=1
        if x==600:
            dir=0
    if dir==0:
        x-=1
        if x==0:
            dir=1
    if dir_1==1:
        y+=1
        if y==400:
            dir_1=0
    if dir_1==0:
        y-=1
        if y==0:
            dir_1=1
    if der==1:
        x_1+=1
        if x_1==650:
            der=0
    if der==0:
        x_1-=1
        if x_1==0:
            der=1
    if der_1==1:
        y_2+=1
        if y_2==450:
            der_1=0
    if der_1==0:
        y_2-=1
        if y_2==50:
            der_1=1
    
    win.fill((255,255,255))
    pygame.draw.rect(win,(255,255,0),(x,y,100,100))
    pygame.draw.circle(win,(0,255,234),(x_1,y_2),50)
    pygame.display.update()
    
    pygame.time.delay(10)
    


















from tkinter import *
H = 500
W = 800
window = Tk()
window.title('Boblejagt')
l = Canvas(window, width=W, height=H, bg='darkblue')
l.pack()

#Laver ubåden
ubaad_id = l.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
ubaad_id2 = l.create_oval(0, 0, 30, 30, outline='red')
UBAAD_R = 15
MID_X = W / 2
MID_Y = H / 2
l.move(ubaad_id, MID_X, MID_Y)
l.move(ubaad_id2, MID_X, MID_Y)

#får ubåden til at bevæge sig
UBAAD_SPEED = 20
def flyt_ubaad(event):
    tast = event.keysym
    if tast == 'Up':
        l.move(ubaad_id, 0, -UBAAD_SPEED)
        l.move(ubaad_id2, 0, -UBAAD_SPEED)
    elif tast == 'Down':
        l.move(ubaad_id, 0, UBAAD_SPEED)
        l.move(ubaad_id2, 0, UBAAD_SPEED)
    elif tast == 'Left':
        l.move(ubaad_id, -UBAAD_SPEED, 0)
        l.move(ubaad_id2, -UBAAD_SPEED, 0)
    elif tast == 'Right':
        l.move(ubaad_id, UBAAD_SPEED, 0)
        l.move(ubaad_id2, UBAAD_SPEED, 0)
l.bind_all('<Key>', flyt_ubaad)


#Laver bobbel
from random import randint
bob_id = list()
bob_r = list()
bob_fart = list()
MIN_BOB_R = 10
MAX_BOB_R = 30
MAX_BOB_FART = 10
GAB = 100
def lav_bobbel():
    x = W + GAB
    y = randint(0, H)
    r = randint(MIN_BOB_R, MAX_BOB_R)
    id1 = l.create_oval(x - r, y - r, x + r, y + r, outline='white')
    bob_id.append(id1)
    bob_r.append(r)
    bob_fart.append(randint(1, MAX_BOB_FART))

def flyt_bobler():
    for i in range(len(bob_id)):
        l.move(bob_id[i], -bob_fart[i], 0)

def faa_koord(id_tal):
    hvor = l.coords(id_tal)
    x = (hvor[0] + hvor[2])/2
    y = (hvor[1] + hvor[3])/2
    return x, y

def slet_boble(i):
    del bob_r[i]
    del bob_fart[i]
    l.delete(bob_id[i])
    del bob_id[i]

def ryd_bob_op():
    for i in range(len(bob_id)-1, -1, -1):
        x, y = faa_koord(bob_id[i])
        if x < -GAB:
            slet_boble(i)

from math import sqrt
def afstand(id1, id2):
    x1, y1 = faa_koord(id1)
    x2, y2 = faa_koord(id2)
    return sqrt((x2 -x1)**2 + (y2 - y1)**2)

def kollision():
    point = 0
    for bob in range(len(bob_id)-1, -1, -1):
        if afstand(ubaad_id2, bob_id[bob]) < (UBAAD_R + bob_r[bob]):
            point += (bob_r[bob] + bob_fart[bob])
            slet_boble(bob)
    return point

l.create_text(50, 30, text='TID', fill='white')
l.create_text(150, 30, text='Score', fill='white')
tid_tekst = l.create_text(50, 50, fill='white')
score_tekst = l.create_text(150, 50, fill='white')
def vis_score(score):
    l.itemconfig(score_tekst, text=str(score))
def vis_tid(tid_rest):
    l.itemconfig(tid_tekst, text=str(tid_rest))




    


from time import sleep, time
BOB_CHANCE = 10
TIDSFRIST = 30
BONUS_SCORE = 1500
score = 0
bonus = 0
slut = time() + TIDSFRIST
#SPILLETS HOVEDLØKKE
while time() < slut:
    if randint(1, BOB_CHANCE) == 1:
        lav_bobbel()
    flyt_bobler()
    ryd_bob_op
    score += kollision()
    if (int(score / BONUS_SCORE)) > bonus:
        bonus += 1
        slut += TIDSFRIST
    vis_score(score)
    vis_tid(int(slut - time()))
    window.update()
    sleep(0.01)



l.create_text(MID_X, MID_Y, text='GAME OVER', fill='white')
l.create_text(MID_X, MID_Y + 30, text='SCORE', fill='white')
l.create_text(MID_X, MID_Y + 45, text=str(score), fill='red')


    



        
        

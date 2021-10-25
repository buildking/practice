import sys
import math
import tkinter.messagebox as msbox
import time
import tkinter.ttk as ttk
from tkinter import *
import random

root = Tk()
root.title('진지한_게임')
root.geometry('640x480+800+100') # 가로 * 세로 + x좌표 + y좌표

Game_Ground = Frame(root)
Game_Ground.pack(side='top')
Start_Ground = Frame(root)
Start_Ground.pack(side='bottom')

def bp(num) :
    print('sik')


ransort=[0 for i in range(20)]

for i in range(1,17):
    globals()['dom_{}'.format(i)]=StringVar(root, value=ransort[i])

print(dom_1.get())
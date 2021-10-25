import tkinter.messagebox as msbox
import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('easy_exel')
root.geometry('640x480+800+100') # 가로 * 세로 + x좌표 + y좌표

Label(root, text='메뉴를 선택하는테치').pack(side='top')

Button(root, text='주문하기').pack(side='bottom')

#burger frame
frame_burger = Frame(root, relief='solid',bd=1)
frame_burger.pack(side='left', fill='both', expand=True)
Button(frame_burger, text='hamburger').pack()
Button(frame_burger, text='cheezeburger').pack()
Button(frame_burger, text='umburger').pack()

#drink frame
frame_drink = LabelFrame(root, text='drink')
frame_drink.pack(side='right', fill='both', expand=True)
Button(frame_drink, text='cola').pack()
Button(frame_drink, text='sider').pack()


root.mainloop()


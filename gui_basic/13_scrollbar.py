import tkinter.messagebox as msbox
import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('easy_exel')
root.geometry('640x480+800+100') # 가로 * 세로 + x좌표 + y좌표

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

#set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode='extended', height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32): # 1~31일
    listbox.insert(END, str(i) + '일') # 1일, 2일,...
listbox.pack(side='left')

scrollbar.config(command=listbox.yview)





root.mainloop()


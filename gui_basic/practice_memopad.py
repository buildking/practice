import os
import pickle
import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('제목 없음 - Window 메모장')
root.geometry('640x480+800+100') # 가로 * 세로 + x좌표 + y좌표

mn='mynote.txt'

#open file(menu)
def open_file():
    if os.path.isfile(mn):#파일 있으면 True, 없으면 False
        with open(mn, 'r') as file:
            txt.delete('1.0', END)#텍스트위젯 본문 삭제
            txt.insert(END, file.read())


#save file(menu)
def save_file():
    with open(mn, 'w') as file:
        file.write(txt.get('1.0',END))#모든 내용을 가져와서 저장


#menu
menu = Menu(root)

#File menu
menu_file = Menu(menu, tearoff=0)

menu_file.add_command(label='열기', command=open_file)
menu_file.add_command(label='저장', command=save_file)
menu_file.add_separator()
menu_file.add_command(label='끝내기', command=root.quit)

menu.add_cascade(label='파일', menu=menu_file)


#etc menu(empty)
menu.add_cascade(label='편집')
menu.add_cascade(label='서식')
menu.add_cascade(label='보기')
menu.add_cascade(label='도움말')

#scrollbar

scrollbar = Scrollbar(root)
scrollbar.pack(side='right', fill='y')



#memos
txt=Text(root,yscrollcommand=scrollbar.set)
txt.pack(side='left',fill='both', expand=True)

##set이 없으면 스크롤을 내려도 다시 올라옴
scrollbar.config(command=txt.yview)







root.config(menu=menu)
root.mainloop()


import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('easy_exel')
root.geometry('640x480+800+100') # 가로 * 세로 + x좌표 + y좌표

def create_new_file():
    print('새 파일을 만드는테치')

menu = Menu(root)


#File menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='New File', command=create_new_file)
menu_file.add_command(label='New window')
menu_file.add_separator()
menu_file.add_command(label='Open file..')
menu_file.add_separator()
menu_file.add_command(label='Saver All', state='disable')#비활성화
menu_file.add_separator()
menu_file.add_command(label='Exit', command=root.quit)

menu.add_cascade(label='file', menu=menu_file)


#Edit menu(빈 값)
menu.add_cascade(label='Edit')

#Language 메뉴 추가(radio버튼을 통해서 택 1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label='Python')
menu_lang.add_radiobutton(label='Java')
menu_lang.add_radiobutton(label='Cpp')
menu.add_cascade(label='Language', menu=menu_lang)

#View 메뉴, 체크버튼(O/X)
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label='Show Minimap')
menu.add_cascade(label='View', menu=menu_view)





root.config(menu=menu)
root.mainloop()


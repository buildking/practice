import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('easy_exel')
root.geometry('640x480+800+100') # 가로 * 세로 + x좌표 + y좌표

valus = [str(i)+'일' for i in range(1, 32)]#1~31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=valus)
combobox.set('카드결제일')#최초목록 제목 설정
combobox.pack()


readonly_combobox = ttk.Combobox(root, height=10, values=valus, state='readonly')#읽기 전용
readonly_combobox.current(0)#0번째 인덱스 값 선택
readonly_combobox.pack()


def btncmd():
    print(combobox.get())#선택된 값 표시
    print(readonly_combobox.get())

btn=Button(root, text='선택', command=btncmd)
btn.pack()

root.mainloop()


from tkinter import *

root = Tk()
root.title('easy_exel')
root.geometry('640x480+800+100') # 가로 * 세로 + x좌표 + y좌표

chkvar = IntVar() #chvar에 int 형으로 값을 저장한다.
chkbox=Checkbutton(root, text='오늘 하루 뷰지 않기', variable=chkvar)
#chkbox.select() #자동 선택 처리
#chkbox.deselect() #선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text='일주일동안 뷰지 않기', variable=chkvar2)
chkbox2.pack()


def btncmd():
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크 됨.
    print(chkvar2.get())




btn=Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()


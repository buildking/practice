import tkinter.messagebox as msbox
import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('easy_exel')
root.geometry('640x480+800+100') # 가로 * 세로 + x좌표 + y좌표

#기차 예매 시스템으로 가정
def info():
    msbox.showinfo('알림','정상적으로 예매 완료된테치.')

def warn():
    msbox.showwarning('경고','해당좌석은 매진된테치.')

def error():
    msbox.showerror('에러','결제오류가 발생된테치.')

def okcancel():
    msbox.askokcancel('확인/취소','해당좌석은 유아동반석인테치. 예매할거임?')
def retrycancel():
    response = msbox.askretrycancel('재시도/취소','일시적인 오류인테치. 재시도?')
    print('응답:', response) #True False none -> yes-1 no-0 etc-cancel
    if response==1:#재시도
        print('재시도')
    elif response==0:#취소
        print('취소')


def yesno():
    msbox.askyesno('예 / 아니오','해당좌석은 역방향인테치. 예매?')
def yesnocancel():
    response = msbox.askyesnocancel(title=None,message='예매내역이 저장되지 않은테치. \n저장안하고 종료하는레후?')
    #네 : 저장 후 종료
    #아니오 : 저장 하지 않고 종료
    #취소 : 프로그램 종료 취소 (현재화면에서 계속 작업)
    print('응답:', response) #True False none -> yes-1 no-0 etc-cancel
    if response==1:#네, ok
        print('예')
    elif response==0:#아니오
        print('아니오')
    else:
        print('취소')





Button(root, command=info, text='알림').pack()
Button(root, command=warn, text='경고').pack()
Button(root, command=error, text='에러').pack()

Button(root, command=okcancel, text='확인 취소').pack()
Button(root, command=retrycancel, text='재시도 취소').pack()
Button(root, command=yesno, text='예 아니오').pack()
Button(root, command=yesnocancel, text='예 아니오 취소').pack()







root.mainloop()


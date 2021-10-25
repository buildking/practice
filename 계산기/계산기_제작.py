import sys
import math
import tkinter.messagebox as msbox
import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('사칙연산_계산기')
root.geometry('640x480+800+100') # 가로 * 세로 + x좌표 + y좌표

btgroup = Frame(root)
btgroup.pack(side='bottom')
rebox = Frame(root)
rebox.pack(side='top')

#연산기호 앞 수
hap1=0
#연산기호 뒤 수
hap2=0
#마지막으로 한 연산
lacal = 0
#결과 출력 상태 저장함수
at = False

#숫자 모두 clear
def cle():
    global hap1
    global hap2
    global re
    global lacal
    global at

    lacal = 0

    hap1 = 0

    at = False

    re.delete(0, 'end')

#소수점으로 int형 변환시 에러날 경우, float로 반환
def flfi(value):
    try:
        int(value)
        return int(value)
    except ValueError:
        return float(value)
#정수로 표현 가능한 수는 정수로 반환
def inch(value):
    if int(value) == float(value):
        return int(value)
    else :
        return float(value)

#연산 함수
def mabt(value):
    global operation  #함수 바깥의 글로벌 변수사용
    global hap1
    if not hap2.get() == '': #기존에 입력한 숫자가 있을때만 연산버튼 인식
        operation = value
        #float filter 함수 호출
        hap1 = flfi(hap2.get()) #입력된 숫자를 임시변수로 옮기고,
        re.delete(0,'end')  #입력칸을 비우고, 다음숫자를 입력받을 준비.
        print(hap1,operation)
 
# 결과 버튼 처리1
def eqbt():
    global operation
    global hap1
    global at

    #연산자나 숫자가 입력되지 않으면, 실행하지 않음.
    if not (operation =='' and re.get()==''):
        number = int(re.get())
        if operation == '/':
            solution = hap1/number
        elif operation == '*':
            solution = hap1*number
        elif operation == '+':
            solution = hap1+number
        elif operation == '-':
            solution = hap1-number
        
    #정수형 반환 가능한지 체크
    solution = inch(solution)
    # 계산후, 숫자표시칸을 비우고, 계산결과를 표시.
    re.delete(0,'end')
    re.insert(0,solution)
    print(hap1,operation,number,"=",solution)
    operation = ''
    hap1 = 0
    #계산 후 at트리거 True로 변경
    at = True


#버튼 눌렀을때
def bp(value):
    
    global at

    if at :
        re.delete(0,'end')
        at=False

    re.insert('end',value)
    print(value, 'pressed')

hap2 = StringVar(root, value='')

#버튼 눌렀을때
def bp(value):
    
    global at

    if at :
        re.delete(0,'end')
        at=False

    re.insert('end',value)
    print(value, 'pressed')
#버튼 눌렀을때
def bp0(value):
    
    global at

    if at :
        re.delete(0,'end')
        at=False
##엔트리박스 비어있는지는 get으로 확인!!
    if re.get() :
        re.insert('end',value)
        print(value, 'pressed')

hap2 = StringVar(root, value='')


#버튼선언(bt=버튼)
##결과창

re = Entry(rebox, textvariable = hap2, width = 20)
re.grid(row=0, columnspan=1)

##2번째 줄
bt_7 = Button(btgroup, text='7', width=5, height=2, command = lambda:bp(7))
bt_8 = Button(btgroup, text='8', width=5, height=2, command = lambda:bp(8))
bt_9 = Button(btgroup, text='9', width=5, height=2, command = lambda:bp(9))
###command append!!
bt_add = Button(btgroup, text='+', width=5, height=2, command = lambda:mabt('+'))
##그리드 선언
bt_7.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
bt_8.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
bt_9.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
bt_add.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

##3번째 줄
bt_4 = Button(btgroup, text='4', width=5, height=2, command = lambda:bp(4))
bt_5 = Button(btgroup, text='5', width=5, height=2, command = lambda:bp(5))
bt_6 = Button(btgroup, text='6', width=5, height=2, command = lambda:bp(6))
###command append!!
bt_mi = Button(btgroup, text='-', width=5, height=2, command = lambda:mabt('-'))
##그리드 선언
bt_4.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
bt_5.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
bt_6.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
bt_mi.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

##4번째 줄
bt_1 = Button(btgroup, text='1', width=5, height=2, command = lambda:bp(1))
bt_2 = Button(btgroup, text='2', width=5, height=2, command = lambda:bp(2))
bt_3 = Button(btgroup, text='3', width=5, height=2, command = lambda:bp(3))
###command append!!
bt_mu = Button(btgroup, text='*', width=5, height=2, command = lambda:mabt('*'))
##그리드 선언
bt_1.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
bt_2.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
bt_3.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
bt_mu.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

##5번째 줄
###command append!!
bt_cl = Button(btgroup, text='clear', width=5, height=2, command = lambda:cle())
bt_0 = Button(btgroup, text='0', width=5, height=2, command = lambda: bp0(0))
bt_eq = Button(btgroup, text='=', width=5, height=2, command = lambda:eqbt())
bt_div = Button(btgroup, text='/', width=5, height=2, command = lambda:mabt('/'))
##그리드 선언
bt_cl.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
bt_0.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
bt_eq.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
bt_div.grid(row=4, column=3, sticky=N+E+W+S, padx=3, pady=3)



# ######흔적기관############################################
# #plus button
# def adbt():
#     global hap2
#     global hap1
#     global re
#     global lacal

#     lacal = 1

#     hap1 = hap1 + hap2
    
#     re.delete(0, 'end')
    
# #minus button
# def mibt():
#     global hap2
#     global hap1
#     global re
#     global lacal

#     lacal = 2

#     hap1 = hap1 - hap2
    
#     re.delete(0, 'end')

# #multiple button
# def mubt():
#     global hap2
#     global hap1
#     global re
#     global lacal

#     lacal = 3

#     hap1 = hap1 * hap2
    
#     re.delete(0, 'end')

# #divide button
# def dibt():
#     global hap2
#     global hap1
#     global re
#     global lacal

#     lacal = 4

#     hap1 = hap1 / hap2
    
#     re.delete(0, 'end')

# #equal button
# def eqbt():
#     global hap2
#     global hap1
#     global re
#     global lacal

#     cocl = 0


#     if lacal == 1:

#         cocl = hap1 + hap2
#         hap1 = 0
#         hap2 = 0

#         lacal = 0

#         re.delete(0, 'end')
#         re.insert('end',cocl)

#     elif lacal == 2:

#         cocl = hap1 - hap2
#         hap1 = 0
#         hap2 = 0

#         lacal = 0

#         re.delete(0, 'end')
#         re.insert('end',cocl)

#     elif lacal == 3:

#         cocl = hap1 * hap2
#         hap1 = 0
#         hap2 = 0

#         lacal = 0

#         re.delete(0, 'end')
#         re.insert('end',cocl)

#     elif lacal == 4:

#         cocl = hap1 / hap2
#         hap1 = 0
#         hap2 = 0

#         lacal = 0

#         re.delete(0, 'end')
#         re.insert('end',cocl)
######흔적기관############################################
    
###################################################
##흔적기관##
# # ns = number sort
# def ns():
    
#     global hap2

#     hap2 = 0

#     jr = len(bg)

#     for i in len(jr):
#         hap2 = hap2 + bg[i]*(10**(jr-i))

#     print(hap2)
####################################################


root.mainloop()
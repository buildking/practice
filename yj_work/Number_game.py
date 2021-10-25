import sys
import math
import tkinter.messagebox as msbox
import time
import tkinter.ttk as ttk
from tkinter import *
from random import *
import threading

root = Tk()
root.title('진지한_게임')
root.geometry('640x480+800+100') # 가로 * 세로 + x좌표 + y좌표

Game_Ground = Frame(root)
Game_Ground.pack(side='top')
Start_Ground = Frame(root)
Start_Ground.pack(side='bottom')

staop = 0
start = time.time()

def bp_start() :
    global start, bt_start
    global staop
    global bt
    global ransort
    global numberry
    global thr

    #thread creat
    thr = threading.Thread(target=time_thread)
    thr.daemon = True
    thr.start()

    #press start_button
    if staop == 0 :
        print('press_start')
        start = time.time()
#        staop = 1
        lambda : time_thread()
#        bt_start.configure(text='stop')
        numberry = 0

        #화면에 표시될 임의의 숫자
        ransort=[i for i in range(16)]
        #ransort에 랜덤 주입
        shuffle(ransort)

        for nu in range(16):
            bt[nu].configure(text=ransort[nu])


    # else :
    #     print('press_stop')
    #     start = 0
    #     staop = 0
    #     bt_start.configure(text='start')



def bp(num) :
    global ransort
    global dom
    global start
    global bt
    global numberry
    global bt_start
    
    #무슨버튼을 눌렀나?
    print(f'print_{num}button')

    #버튼 제대로 눌렀나?
    if numberry == ransort[num]:

        end = time.time()
        # #start버튼에 시간초 표시
        # bt_start.configure(text=str(end-start))

        bt[num].configure(text='X')

        #마지막까지 오면 통과
        if numberry == 15 : 
            msbox.showinfo(int(end-start), '성공!')
#            sys.exit(print((end-start), 'Best_gamer!'))
            bp_start()
        
        #다음 넘베리 +1
        numberry += 1

    else :
        msbox.showwarning(numberry, '실패!')
        sys.exit(print('game_over!'))





#dom[i] bp[i] i로 연동!!

bt = []

bt=[0 for i in range(20)]

#버튼 16종 만들기
for i in range(16):
    bt[i] = Button(Game_Ground, text = 'start click!', width=10, height=5, command = lambda um = i : bp(um))
    bt[i].grid(row=i//4, column=i%4, sticky=N+E+W+S, padx=3, pady=3)

#start버튼 만들기
bt_start = Button(Start_Ground, text = 'start', width=16, height=8, command=lambda:bp_start())
bt_start.pack()


def time_thread() :
    global bt_start, reti
    reti = time.time()
    bt_start.configure(text=int(reti-start))
    threading.Timer(1, time_thread).start()




### #그릇에 숫자 담기
# dom[1]=StringVar(root, value=ransort[1])
# dom[2]=StringVar(root, value=ransort[2])
# dom[3]=StringVar(root, value=ransort[3])
# dom[4]=StringVar(root, value=ransort[4])
# dom[5]=StringVar(root, value=ransort[5])
# dom[6]=StringVar(root, value=ransort[6])
# dom[7]=StringVar(root, value=ransort[7])
# dom[8]=StringVar(root, value=ransort[8])
# dom[9]=StringVar(root, value=ransort[9])
# dom[10]=StringVar(root, value=ransort[10])
# dom[11]=StringVar(root, value=ransort[11])
# dom[12]=StringVar(root, value=ransort[12])
# dom[13]=StringVar(root, value=ransort[13])
# dom[14]=StringVar(root, value=ransort[14])
# dom[15]=StringVar(root, value=ransort[15])
# dom[16]=StringVar(root, value=ransort[16])




# bt[1] = Button(Game_Ground, text = 'start click!', width=10, height=5, command = lambda : bp(1))
# bt[1].grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)


# bt[2] = Button(Game_Ground, text = 'start click!', width=10, height=5, command = lambda:bp(2))
# bt[3] = Button(Game_Ground, text = 'start click!', width=10, height=5, command = lambda:bp(3))
# bt[4] = Button(Game_Ground, text = 'start click!', width=10, height=5, command = lambda:bp(4))
# bt[5] = Button(Game_Ground, text = 'start click!', width=10, height=5, command = lambda:bp(5))
# bt[6] = Button(Game_Ground, text = 'start click!', width=10, height=5, command = lambda:bp(6))
# bt[7] = Button(Game_Ground, text = 'start click!', width=10, height=5, command = lambda:bp(7))
# bt[8] = Button(Game_Ground, text = 'start click!', width=10, height=5, command = lambda:bp(8))
# bt[9] = Button(Game_Ground, text = 'start click!', width=10, height=5, command = lambda:bp(9))
# bt[10] = Button(Game_Ground, text = 'start click!', width=10, height=5, command = lambda:bp(10))
# bt[11] = Button(Game_Ground, text = 'start click!', width=10, height=5, command = lambda:bp(11))
# bt[12] = Button(Game_Ground, text = 'start click!', width=10, height=5, command = lambda:bp(12))
# bt[13] = Button(Game_Ground, text = 'start click!', width=10, height=5, command = lambda:bp(13))
# bt[14] = Button(Game_Ground, text = 'start click!', width=10, height=5, command = lambda:bp(14))
# bt[15] = Button(Game_Ground, text = 'start click!', width=10, height=5, command = lambda:bp(15))
# bt[16] = Button(Game_Ground, text = 'start click!', width=10, height=5, command = lambda:bp(16))

# #버튼 그리드
# bt[2].grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
# bt[3].grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
# bt[4].grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)
# bt[5].grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
# bt[6].grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
# bt[7].grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
# bt[8].grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)
# bt[9].grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
# bt[10].grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
# bt[11].grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
# bt[12].grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)
# bt[13].grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
# bt[14].grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
# bt[15].grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
# bt[16].grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

root.mainloop()
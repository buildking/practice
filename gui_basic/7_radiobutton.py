from tkinter import *

root = Tk()
root.title('easy_exel')
root.geometry('640x480+800+100') # 가로 * 세로 + x좌표 + y좌표

Label(root, text='메뉴를 선택하는테치').pack()

burger_var = IntVar() #여기에 int형으로 값을 저장한다.
btn_burger1 = Radiobutton(root, text='햄버거',value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text='띠드버거',value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text='카우버거',value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text='select drink').pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root,text='cola', value = 'cola', variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root,text='sider', value = 'sider', variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(burger_var.get())#햄버거 중 선택된 라디오 항목의 값(value)를 출력
    print(drink_var.get())#음료중 선택된 값을 출력


btn=Button(root, text='주문', command=btncmd)
btn.pack()

root.mainloop()


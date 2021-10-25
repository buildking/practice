from tkinter import *

root = Tk()
root.title('easy_exel')
root.geometry('640x480+800+100') # 가로 * 세로 + x좌표 + y좌표

listbox=Listbox(root, selectmode='extended', height=0)
listbox.insert(0,'apple')
listbox.insert(1,'berry')
listbox.insert(2,'banana')
listbox.insert(END, 'water_melon')
listbox.insert(END, 'grape')
listbox.pack()



def btncmd():
    #listbox.delete(END) #맨 뒤 삭제
    #listbox.delete(0)#맨 앞 삭제
    
    #개수 확인
    #print('리스트에는', listbox.size(), '개가있어요')

    # 항목 확인(시작 idx, 끝 idx)
    #print('1번부터 3번까지의 항목 : ', listbox.get(0,2))

    #선택된 항목 확인 (위치로 반환 (ex) (1, 2, 3) )
    print('선택된 항목 : ', listbox.curselection())




btn=Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()


from tkinter import *

root = Tk()
root.title('easy_exel')
root.geometry('640x480')

label1 = Label(root, text= '보이루')
label1.pack()

photo = PhotoImage(file='gui_basic/button_okay.png')
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text='리하이')
    
    global photo2
    photo2 = PhotoImage(file='gui_basic/button_roh.png')
    label2.config(image=photo2)

btn= Button(root, text='클릭', command=change)
btn.pack()


root.mainloop()


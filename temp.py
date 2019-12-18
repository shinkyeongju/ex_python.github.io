from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox

import tkinter.simpledialog


def temper():
    global entry_c, entry_f
    window = Tk()
    window.title('온도 변환 프로그램') # 윈도우 이름
    window.geometry('250x150') # 윈도우 가로 * 세로 사이즈
    label_1 = Label(window, text='온도 변환 프로그램')
    label_2 = Label(window, text = '섭씨')
    label_3 = Label(window, text = '화씨')
    label_1.grid(row=0, column = 0, columnspan =2)        # label 위젯을 윈도우에 배치 , span --> 열이나 행을 합치는 것
    label_2.grid(row=1, column = 0)
    label_3.grid(row=2, column = 0)



    entry_c = Entry(window)
    entry_f = Entry(window)

    entry_c.grid(row=1, column=1)
    entry_f.grid(row=2, column=1)                      # 형식 : Entry(객체명, 속성)

    btn_1=Button(window, text='섭씨 -> 화씨', command = cTof)
    btn_2=Button(window, text='화씨 -> 섭씨', command = fToc)

    btn_1.grid(row=3, column = 0)
    btn_2.grid(row=3, column = 1)
    window.mainloop()
    
def cTof():
    global entry_f
    c = float(entry_c.get())
    f = 9.0/5.0*c+32.0
    entry_c.delete(0,END)
    entry_f.insert(0,str(f))


def fToc():
    global entry_c
    f = float(entry_f.get())
    c = 5.0/9.0*(f-32.0)
    entry_f.delete(0,END)
    entry_c.insert(0,str(c))  
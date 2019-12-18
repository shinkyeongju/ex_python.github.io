from tkinter import *



def cal():
    global col_index, s
    window = Tk()
    window.title('My Calculator')
    display = Entry(window, width = 33, bg = 'pink')
    display.grid(row = 0, column = 0, columnspan = 5)
    bt_list = '7,8,9,/,C,4,5,6,*,%,1,2,3,-,**,0,,=,+,←'.split(",")
    print(bt_list)

    col_index = 0
    row_num = 1
    for button_text in bt_list:       # command =lambda x = button_text : click(x) --> button_text 가 x로 가고 x가 click()으로 간다.
        Button(window, text=button_text, width = 5, command =lambda x = button_text : click(x)).grid(row = row_num, column = col_index)
    #     btn = Button(window, text=bt_text, width = 5)
    #     btn.grid(row = row_num, column = col_index)              
        col_index += 1
        if col_index == 5:      # row 변경 해주는 code
            row_num+=1
            col_index = 0
    def click(key):
        if key == '=':
            result = eval(display.get())
            s = str(result)
            display.insert(END, '=' + s)
        elif key == 'C':
            display.delete(0, END)               # delete(시작점,끝점) --> 시작점부터 끝점까지 지운다.
        elif key == '←':
            size = len(display.get())
            display.delete(size-1,END)
        else: display.insert(END, key)
    window.mainloop()
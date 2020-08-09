print('Hello Pie IM!')

import sys
import os
import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import *

try:
    print(sys.argv[1])
except:
    warn_win=tk.Tk()
    warn_win.withdraw()
    msgbox.showwarning('警告','请先进行登录！')
    os.system("python ./login.py")
    exit()

win=tk.Tk()
win.geometry('360x480')
win.title('Pie IM')
win.iconbitmap("./icons/icon-mini.ico")

chatList=tk.Listbox(win,width=30)
chatList.pack(side=LEFT,fill=BOTH,expand=True)

win.mainloop()
import tkinter as tk
import time

s_win=tk.Tk()
s_win.overrideredirect(1)

s_win.title('Windows美化助手')
screenWidth = s_win.winfo_screenwidth()  # 获取显示区域的宽度
screenHeight = s_win.winfo_screenheight()  # 获取显示区域的高度
width = 300  # 设定窗口宽度
height = 150  # 设定窗口高度
left = (screenWidth - width) / 2
top = (screenHeight - height) / 2
s_win.geometry("%dx%d+%d+%d" % (width, height, left, top))

text=tk.Label(s_win,text='Windows美化助手',font=('幼圆',25),bg='DodgerBlue',fg='white',width=320,height=150)
text.pack()

by=tk.Label(s_win,text='2020 By 人工智障',bg='DodgerBlue',fg='black',font=('幼圆',5))
by.pack()


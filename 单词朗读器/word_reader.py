import tkinter as tk
import time
import easygui

s_win=tk.Tk()
s_win.overrideredirect(1)
s_win.title('单词朗读程序')
screenWidth = s_win.winfo_screenwidth()  # 获取显示区域的宽度
screenHeight = s_win.winfo_screenheight()  # 获取显示区域的高度
width = 300  # 设定窗口宽度
height = 150  # 设定窗口高度
left = (screenWidth - width) / 2
top = (screenHeight - height) / 2
s_win.geometry("%dx%d+%d+%d" % (width, height, left, top))

text=tk.Label(s_win,text='单词朗读程序',font=('幼圆',25),bg='DodgerBlue',fg='white',width=320,height=270)
text.pack()

s_win.update()

time.sleep(2)
s_win.destroy()


def choose():
    easygui.fileopenbox(title='选择图片',filetypes=[['*.jpg','*.png','图片文件']])

win=tk.Tk()
win.title('单词朗读程序')

enterbox=tk.Text(win,font=('幼圆',12))
enterbox.pack(fill=tk.BOTH)

choose_btn=tk.Button(win,text='选择图片',font=('幼圆',15),height=2,bg='DodgerBlue',fg='white',command=choose)
choose_btn.pack(padx=20,pady=30,fill=tk.X)

win.mainloop()

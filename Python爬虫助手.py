import requests
import tkinter as tk
from tkinter import *
import tkinter.messagebox as msgbox
from tkhtmlview import HTMLLabel
print('库导入完毕')

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}

def get(link):
    import requests
    response = requests.get(url=link)
    response.encoding = 'utf-8'
    print(response)
    # 返回响应状态码
    print(response.status_code)  # 200
    # 返回响应文本
    print(response.text)
    print(type(response.text))
    html=response.text
    return html

def view(html):
    viewWin=tk.Tk()
    inputbox=tk.Text(viewWin,width='1',font=('Courier New',10))
    inputbox.place(side=LEFT)
    inputbox.insert(END,html)
    outputbox=HTMLLabel(viewWin, width='1', background='white', html=html)
    outputbox.pack(side=RIGHT)
    outputbox.fit_height()
    viewWin.mainloop()

def start():
    link=linkEnter.get()
    if link!='':
        html=get(link)
        view(html)
    else:
        msgbox.showwarning('警告','必须输入链接')

win=tk.Tk()
win.geometry('800x450')
win.title('Python 爬虫助手')
linkEnterTip=tk.Label(win,text='将链接粘贴在此处',font=('幼圆',15))
linkEnterTip.place(x=30,y=20)
linkEnter=tk.Entry(win,width=50)
linkEnter.place(x=30,y=50)
startBtn=tk.Button(win,text='开始',fg='white',bg='green',font=('幼圆',15),command=start)
startBtn.place(x=30,y=100)
win.mainloop()

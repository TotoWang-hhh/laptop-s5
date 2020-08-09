#函数
def bei(numList):
    okList=[]
    num=1
    while True:
        okList=[]
        for i in numList:
            if num%int(i)==0:
                okList.append(True)
        if len(okList)==len(numList):
            return num
            break
        else:
            num+=1
            print('调试信息：尝试%s'%num)

def yin(numList):
    messagebox.showwarning('注意','请不要继续！这个功能还在制作！请在单击“确定”后手动重启程序！')
    exit()
    temp=0
    okList=[]
    num=1
    while True:
        if int(temp)%num==0:
            if int(temp)<num:
                num+=1
                print('调试信息：尝试%s'%num)
            else:
                okList.append(True)
        if len(okList)==len(numList):
            return num
            break
        else:
            num+=1
            print('调试信息：尝试%s'%num)

def func():
    choice=v.get()
    print('调试信息：choice=%s'%choice)
    num_enter=num_enterbox.get()
    if num_enter=='':
        print('\033[37;43m\t警告！请务必输入需要计算的数')
    num_list=num_enter.split(',')
    global ans
    ans=0
    if choice==1:
        ans=yin(num_list)
    elif choice==2:
        ans=bei(num_list)
    else:
        print('\033[37;41m\t程序错误！')
    print(ans)
    res_show["text"]="结果："+str(ans)

def webOpen():
    web.open("https://totowang-hhh.github.io/index.html")

#界面
try:
    import tkinter as tk
    from tkinter import *
    import tkinter.messagebox as messagebox
except:
    con=messagebox.askyesno('是否继续？', '该程序对Python 3的兼容性更加，是否继续？')
    if con:
        import Tkinter as tk
        from Tkinter import *
        import Tkinter,messagebox as messagebox
    else:
        exit()
import webbrowser as web
import time

window=tk.Tk()
window.geometry('800x450')
window.title('最大公因数与最小公倍数计算器')
window.resizable(0,0)

webBtn=tk.Button(window,text='By 人工智障',
                 width=110,height=2,bd=3,fg='white',bg='blue',
                 command=webOpen)
webBtn.place(x=10,y=10)

enter_num_tip=tk.Label(window,text='请输入一切将要计算的数，用英文逗号分隔')
enter_num_tip.place(x=10,y=100)
num_enterbox=tk.Entry(window,bd=2,show=None,width=100)
num_enterbox.place(x=10,y=125)

v=IntVar()
v.set(2)
Radiobutton(window,text='最大公因数',variable=v,value=1,).place(x=10,y=200,
                                                           anchor=W)
Radiobutton(window,text='最小公倍数',variable=v,value=2,).place(x=10,y=220,
                                                           anchor=W)

runBtn=tk.Button(window,text='立即计算',bd=3,width=100,height=2,command=func)
runBtn.place(x=10,y=300)

res_show=tk.Label(window,text="结果：")
res_show.place(x=350,y=200)

window.mainloop()

#face=tk.Label(window,text='·u·')
#face.place(x=350,y=250)
#ci=0
#while ci<3:
#    face['text']='·u·'
#    time.sleep(2)
#    window.mainloop()
#    face['text']='·u<'
#    time.sleep(1)
#    window.mainloop()
#    ci+=1

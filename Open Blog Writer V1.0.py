import tkinter as tk
from tkinter import *
from tkinter import font , filedialog
from markdown2 import Markdown
from tkhtmlview import HTMLLabel

window=tk.Tk()
window.title('Open Blog Writer')
window.geometry('800x450')

def onInputChange():
    self.inputeditor.edit_modified(0)
    md2html = Markdown()
    outputbox.set_html(md2html.convert(inputeditor.get("1.0" , END)))
    markdownText = self.inputeditor.get("1.0" , END)
    html = md2html.convert(markdownText)
    outputbox.set_html(html)

def openfile():
    openfilename = filedialog.askopenfilename(filetypes=(("Markdown File", "*.md , *.mdown , *.markdown"),
                                                        ("Text File", "*.txt"),
                                                        ("All Files", "*.*")))
    if openfilename:
        try:
            self.inputeditor.delete(1.0, END)
            self.inputeditor.insert(END , open(openfilename).read())
        except:
            print("无法打开文件！")

def savefile():
    filedata = inputeditor.get("1.0" , END)
    savefilename = filedialog.asksaveasfilename(filetypes = (("Markdown File", "*.md"),
                                                             ("Text File", "*.txt")) , title="保存 Markdown 文件")
    if savefilename:
        try:
            f = open(savefilename , "w")
            f.write(filedata)
        except:
            mbox.showerror("保存文件错误" , "哎呀！, 文件: {} 保存错误！".format(savefilename))

myfont = font.Font(family="等线", size=15)
inputeditor = Text(window, width="1")
inputeditor.pack(fill=BOTH, expand=1, side=LEFT)
inputeditor = Text(window, width="1" , font=myfont)
outputbox=HTMLLabel(window, width="1", background="white", html="<h1>linuxidc.com</h1>")
outputbox.pack(fill=BOTH, expand=1, side=RIGHT)
outputbox.fit_height()
mainmenu = Menu(window)
filemenu = Menu(mainmenu)
filemenu.add_command(label="打开", command=openfile)
filemenu.add_command(label="另存为", command=savefile)
filemenu.add_separator()
filemenu.add_command(label="退出", command=quit)
mainmenu.add_cascade(label="文件", menu=filemenu)

window.mainloop()

while True:
    onInputChange()

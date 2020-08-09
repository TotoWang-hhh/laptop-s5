from tkinter import *
from tkinter import font , filedialog
from markdown2 import Markdown
from tkhtmlview import HTMLLabel

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.myfont = font.Font(family="等线", size=15)
        self.init_window()
    def init_window(self):
        self.master.title("linuxidc.com编辑器")
        self.pack(fill=BOTH, expand=1)
        self.inputeditor = Text(self, width="1")
        self.inputeditor.pack(fill=BOTH, expand=1, side=LEFT)
        self.inputeditor = Text(self, width="1" , font=self.myfont)
        self.outputbox=HTMLLabel(self, width="1", background="white", html="<h1>linuxidc.com</h1>")
        self.outputbox.pack(fill=BOTH, expand=1, side=RIGHT)
        self.outputbox.fit_height()
        self.inputeditor.bind("<<Modified>>", self.onInputChange)
        self.pack(fill=BOTH, expand=1)
        self.mainmenu = Menu(self)
        self.filemenu = Menu(self.mainmenu)
        self.filemenu.add_command(label="打开", command=self.openfile)
        self.filemenu.add_command(label="另存为", command=self.savefile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="退出", command=self.quit)
        self.mainmenu.add_cascade(label="文件", menu=self.filemenu)
        self.master.config(menu=self.mainmenu)
    def openfile(self):
        openfilename = filedialog.askopenfilename(filetypes=(("Markdown File", "*.md , *.mdown , *.markdown"),
                                                             ("Text File", "*.txt"),
                                                             ("All Files", "*.*")))
        if openfilename:
            try:
                self.inputeditor.delete(1.0, END)
                self.inputeditor.insert(END , open(openfilename).read())
            except:
                print("无法打开文件！")
    def onInputChange(self , event):
        self.inputeditor.edit_modified(0)
        md2html = Markdown()
        self.outputbox.set_html(md2html.convert(self.inputeditor.get("1.0" , END)))
        markdownText = self.inputeditor.get("1.0" , END)
        html = md2html.convert(markdownText)
        self.outputbox.set_html(html)

root=Tk()
root.geometry("800x600")
app=Window(root)
app.mainloop()

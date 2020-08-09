import time
import threading
import os
import sys

def load(doing,times):
    t=0
    while t<=times:
        load=doing+' .  '
        print('\r'+load,end='',flush=True)
        time.sleep(0.3)
        load=doing+' .. '
        print('\r'+load,end='',flush=True)
        time.sleep(0.3)
        load=doing+' ...'
        print('\r'+load,end='',flush=True)
        time.sleep(0.3)
        t+1
    print('\n')

def load_c():
    while True:
        load='▀　'
        print('\r'+load,end='',flush=True)
        time.sleep(0.3)
        load='　▀'
        print('\r'+load,end='',flush=True)
        time.sleep(0.3)
        load='　▄'
        print('\r'+load,end='',flush=True)
        time.sleep(0.3)
        load='▄　'
        print('\r'+load,end='',flush=True)
        time.sleep(0.3)

def acc():
    ip='192.168.56.1'
    #if not os.path.isdir("./usr_data/{}/".format(ip)):
        #file=open("./usr_data/{}/chatList.dat",'w',encoding='utf-8')
        #file.write('{}')

t_load=threading.Thread(target=load,args=('Checking settings',10),name='Pie IM自检程序')
t_load.start()
acc()

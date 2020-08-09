import pygame
import time
from sys import exit
import win32api,win32con

#请在下方书写你的代码
pygame.init()
hj=pygame.image.load("./滑稽.png")
win=pygame.display.set_mode((500,500))
win.blit(hj,(10,10))
pygame.display.set_caption('你关掉我试试')
pygame.display.set_icon(hj)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            c=win32api.MessageBox(0,"关不掉我吧","hhh",win32con.MB_OK)
            n=1
            tklist=[]
            while n<=100:
                c=win32api.MessageBox(0, "慢慢清理吧", "你凉了",win32con.MB_OK)
                print(c)
                t=0
            while t<=100:
                if str(c)=='1':
                    t+=1
                    print('清除第{}个弹框'.format(t))
            print('全部清除')
            time.sleep(500)
                
    pygame.display.update()

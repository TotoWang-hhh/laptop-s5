import tkinter as tk
import pygame

tk_win=tk.Tk()
print(tk_win)

pygame_win=pygame.display.set_mode((100,100))
print(pygame_win)

class Sample():
    def __init__(self):
        self.sample='sample'
obj=Sample()
print(obj)

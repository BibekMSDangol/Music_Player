from tkinter import *
import pygame
from PIL import ImageTk, Image

root = Tk()
root.title('Music Player')
root.iconbitmap('IconMu.ico')
root.geometry("960x540")

bg = ImageTk.PhotoImage(Image.open("background.png"))

myLabel = Label(root, image=bg)
myLabel.place(x=0, y=0)

pygame.mixer.init()

all_songs = Listbox(root, bg='white', fg='red', width=60)
all_songs.pack(pady=20)
root.mainloop()

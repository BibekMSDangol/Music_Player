from tkinter import *
import pygame
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title('Music Player')
root.iconbitmap('IconMu.ico')
root.geometry("960x540")


pygame.mixer.init()


def add_song():
    song = filedialog.askopenfilename(initialdir='audio', title="Choose a song", filetypes=(("mp3 Files","*.mp3"), ))
    print(song)



all_songs = Listbox(root, bg='white', fg='red', width=70, height=20)
all_songs.pack(pady=10)

play_image = PhotoImage(file='play.png')
pause_image = PhotoImage(file='pause.png')
stop_image = PhotoImage(file='stop.png')
forward_image = PhotoImage(file='forward.png')
back_image = PhotoImage(file='back.png')

control_frame = Frame(root)
control_frame.pack()

play_button = Button(control_frame, image=play_image, borderwidth=0)
pause_button = Button(control_frame, image=pause_image, borderwidth=0)
stop_button = Button(control_frame, image=stop_image, borderwidth=0)
forward_button = Button(control_frame, image=forward_image, borderwidth=0)
back_button = Button(control_frame, image=back_image, borderwidth=0)

play_button.grid(row=0, column=2)
pause_button.grid(row=0, column=1)
stop_button.grid(row=0, column=3)
forward_button.grid(row=0, column=4)
back_button.grid(row=0, column=0)

my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu()
my_menu.add_cascade(label="Add songs", menu=add_song_menu)
add_song_menu.add_command(label="Add a song to playlist", command=add_song)
root.mainloop()


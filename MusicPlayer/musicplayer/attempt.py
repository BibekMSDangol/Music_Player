from tkinter import *
import pygame
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Music Player')
root.iconbitmap('IconMu.ico')
root.geometry("960x540")

bg = ImageTk.PhotoImage(Image.open("pdp.png"))

myLabel = Label(root, image=bg)
myLabel.place(x=0, y=0)

pygame.mixer.init()


def add_song():
    song = filedialog.askopenfilename(initialdir='Music', title="Select a Song", filetypes=(("mp3 Files","*.mp3"), ))
    song = song.replace("C:/Users/acer/Music/", "")
    song = song.replace(".mp3", "")
    all_songs.insert(END, song)


def play():
    song = all_songs.get(ACTIVE)
    song = f'C:/Users/acer/Music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


def pause():
    pygame.mixer.music.pause()


def stop():
    pygame.mixer.music.stop()
    all_songs.select_clear(ACTIVE)


all_songs = Listbox(root, bg='white', fg='red', width=70, height=20, selectbackground='red')
all_songs.pack(pady=10)

play_image = PhotoImage(file='play.png')
pause_image = PhotoImage(file='pause.png')
stop_image = PhotoImage(file='stop.png')
forward_image = PhotoImage(file='forward.png')
back_image = PhotoImage(file='back.png')

control_frame = Frame(root)
control_frame.pack()

play_button = Button(control_frame, image=play_image, command=play)
pause_button = Button(control_frame, image=pause_image, borderwidth=0, command=pause)
stop_button = Button(control_frame, image=stop_image, borderwidth=0, command=stop)
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
scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(50)
scale.pack(ipadx=50, ipady=10)
root.mainloop()


from tkinter import *
import pygame
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

def music_player():
    root = Toplevel()
    root.title('Music Player')
    root.iconbitmap('IconMu.ico')
    root.geometry("1080x618")

    pygame.mixer.init()

    def play_time():
        current_time = pygame.mixer.music.get_pos()

    def add_songs():
        songs = filedialog.askopenfilenames(initialdir='audio', title="Select any Music", filetypes=(("mp3 Files", "*.mp3"),))
        for song in songs:
            song = song.replace("C:/Users/acer/Music/", "")
            song = song.replace(".mp3", "")
            all_songs.insert(END, song)

    def play():
        song = all_songs.get(ACTIVE)
        song = f'C:/Users/acer/Music/{song}.mp3'
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        play_time()

    global paused
    paused = False

    def pause(is_paused):
        global paused
        paused = is_paused
        if paused:
            pygame.mixer.music.unpause()
            paused = False
        else:
            pygame.mixer.music.pause()
            paused = True


    def stop():
        pygame.mixer.music.stop()
        all_songs.select_clear(ACTIVE)


    def next_song():
        new_song = all_songs.curselection()
        new_song = new_song[0]+1
        song = all_songs.get(new_song)

        song = f'C:/Users/acer/Music/{song}.mp3'
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        all_songs.select_clear(0, END)

        all_songs.activate(new_song)

        all_songs.select_set(new_song, last=None)


    def previous_song():
        new_song = all_songs.curselection()
        new_song = new_song[0] - 1
        song = all_songs.get(new_song)

        song = f'C:/Users/acer/Music/{song}.mp3'
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        all_songs.select_clear(0, END)

        all_songs.activate(new_song)

        all_songs.select_set(new_song, last=None)


    def set_volume(val):
        volume = int(val)/100
        pygame.mixer.music.set_volume(volume)


    all_songs = Listbox(root, bg='white', fg='red', width=70, height=20, selectbackground='red')
    all_songs.pack(pady=10)

    play_image = PhotoImage(file='play.png')
    pause_image = PhotoImage(file='pause.png')
    stop_image = PhotoImage(file='stop.png')
    forward_image = PhotoImage(file='forward.png')
    back_image = PhotoImage(file='back.png')

    control_frame = Frame(root)
    control_frame.pack()

    play_button = Button(control_frame, image=play_image, borderwidth=0, command=play)
    pause_button = Button(control_frame, image=pause_image, borderwidth=0, command=lambda: pause(paused))
    stop_button = Button(control_frame, image=stop_image, borderwidth=0, command=stop)
    forward_button = Button(control_frame, image=forward_image, borderwidth=0, command=next_song)
    back_button = Button(control_frame, image=back_image, borderwidth=0, command=previous_song)

    play_button.grid(row=0, column=1)
    pause_button.grid(row=0, column=2)
    stop_button.grid(row=0, column=3)
    forward_button.grid(row=0, column=4)
    back_button.grid(row=0, column=0)
    volume_Label=Label(control_frame, text="Volume")
    volume_Label.grid(row=5, column=2)

    my_menu = Menu(root)
    root.config(menu=my_menu)

    add_songs_menu = Menu()
    my_menu.add_cascade(label="Add Music", menu=add_songs_menu)
    add_songs_menu.add_command(label="Add any Music to playlist", command=add_songs)

    scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
    scale.set(50)
    scale.pack(ipadx=50, ipady=10)

    root.mainloop()

def ok():
    username = e1.get()
    password = e2.get()

    if(username == "" and password == ""):
        messagebox.showinfo("", "Blank is not allowed")

    elif(username == "admin" and password == "1234"):
        music_player()

    else:
        messagebox.showinfo("", "Incorrect Username or Password")


root = Tk()
root.title("Login")
root.iconbitmap('IconMu.ico')
root.geometry("300x200")
bg = ImageTk.PhotoImage(Image.open("lake.jpg"))
global e1
global e2
Label(root, image=bg).place(x=0,y=0)
Label(root, text="Username :").place(x=5, y=5)
Label(root, text="Password :").place(x=5, y=40)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")

Button(root, text="Login", command=ok, height=2, width=10).place(x=110, y=100)


root.mainloop()
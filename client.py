import socket
from threading import Thread
from tkinter import *
from tkinter import ttk


PORT = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


def musicWindowGUI():

    window = Tk()
    window.title("Music Sharing")
    window.geometry("600x500")
    window.resizable(width=False, height=False)
    window.configure(bg="black")

    userLable = Label(window, bg="black", fg="white", text="Enter You Name :",
                      font=("Comic Sans MS", 15))
    userLable.place(relx=0.04, rely=0.02)

    userEntry = Entry(window, font=("Comic Sans MS", 15), width=30)
    userEntry.place(relx=0.15, rely=0.125)

    connectToServer = Button(window, text="Connect", bg="blue", fg="white",
                             font=("Comic Sans MS", 12), width=7)
    connectToServer.place(relx=0.79, rely=0.120)

    separator = ttk.Separator(window, orient='horizontal')
    separator.place(x=0, rely=0.25, relwidth=1, height=0.1)

    labelusers = Label(window, bg="black", fg="white", text="Active Users:",
                       font=("Comic Sans MS", 10))
    labelusers.place(relx=0.04, rely=0.275)

    listbox = Listbox(window, height=5, width=68,
                      activestyle='dotbox', font=("Comic Sans MS", 10))
    listbox.place(relx=0.04, rely=0.325)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight=1, relx=1)
    scrollbar1.config(command=listbox.yview)

    PlayButton = Button(window, text="Play", bd=1, width=5,
                        font=("Comic Sans MS", 10), bg="green")
    PlayButton.place(relx=0.48, rely=0.55)

    stopButton = Button(window, text="Stop", bd=1, width=5,
                        font=("Comic Sans MS", 10), bg="red")
    stopButton.place(relx=0.58, rely=0.55)

    uploadButton = Button(
        window, text="Upload", bd=1, font=("Comic Sans MS", 10), width=8, bg="yellow")
    uploadButton.place(relx=0.68, rely=0.55)

    downloadButton = Button(window, text="Download",
                            bd=1, font=("Comic Sans MS", 10), width=10, bg="yellow")
    downloadButton.place(relx=0.82, rely=0.55)

    infolable = Label(window, text="", fg="blue", font=("Comic Sans MS", 10))
    infolable.place(relx=0.04, rely=0.6)

    window.mainloop()


def setup():
    global PORT, SERVER, IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindowGUI()


setup()

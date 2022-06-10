from re import T
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk


PORT = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


def acceptConnection():
    global SERVER

    while True:
        conn, addr = SERVER.accept()
        print(f"Connected, {addr}")



def setup():
    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(100)

    acceptConnection()


setup_thread = Thread(target=setup)
setup_thread.start()
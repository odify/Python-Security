#!/usr/bin/env python3


import webbrowser
from tkinter import *

root = Tk()
root.title("WebBrowser")
root.geometry("300x200")


def copyassignment():
    webbrowser.open("www.github.com/odify")


def google():
    webbrowser.open("www.google.com")


copyassignment = Button(root, text="My Github projects", command=copyassignment).pack(pady=20)

mygoogle = Button(root, text="open Google", command=google).pack(pady=20)
root.mainloop()


# importing webbrowser module
import webbrowser
# importing tkinter
from tkinter import *

# creating root
root = Tk()
# setting GUI title
root.title("WebBrowser")
# setting GUI geometry
root.geometry("400x300")


# function to open copyassignment.com in browser
def copyassignment():
    webbrowser.open("www.github.com/trending")


# function to open google in browser
def google():
    webbrowser.open("www.google.com")


# button to call copyassignment function
copyassignment = Button(root, text="Trending Github projects", command=copyassignment).pack(pady=20)
# button to call google function
mygoogle = Button(root, text="open Google", command=google).pack(pady=20)
root.mainloop()


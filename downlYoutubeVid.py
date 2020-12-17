from pytube import YouTube
import pytube

from tkinter import *

root = Tk()

root.geometry("300x400")
root.title("You tube video download")
def youtube():
    a = var.get()#https://www.youtube.com/watch?v=6Ej2BLRtE4Y
    ytvideo = YouTube(a).streams.filter(file_extension="mp4").order_by('resolution').desc().first()

    ytvideo.download(r"G:\games")
    print("Entry box" , a)
l1 = Label(root, text="YouTube Video Link" , fg="Red" , font="bold")
l1.place(x=30 , y=20)

var = StringVar()
e1 = Entry(root , textvariable=var , width=60)
e1.place(x=40 , y=80)

b1 = Button(root , text ="Download" , command=youtube , bg="green" , width=20 , fg="white")
b1.place(x=80 , y=120)




root.mainloop()
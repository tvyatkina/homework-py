from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("youtube video downloader")

Label(root, text='Youtube Video Downloader', font='montserrat 20 bold').pack()
link = StringVar()

Label(root, text='Paste Link Here:', font='montserrat 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=47, textvariable=link).place(x=32, y=60)

def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='DOWNLOADED', font='montserrat 16', bg='#C6DABF').place(x=183, y=210)

Button(root, text='DOWNLOAD', font='montserrat 15 bold', padx=2, command=downloader).place(x=180, y=150)

root.mainloop()
from tkinter import *
from pytube import YouTube
from functions import *

root = Tk()

root.title('Downloader YouTube')
root.geometry("650x350+400+300")# width x height + positionX + positionY
root.resizable(True, True)# height, width

lblTitle = Label(root, text='-------------------- MENU --------------------', font='bold')
lblTitle.config(font=40)
lblTitle.pack()

lblLink = Label(root, text='\nPaste here the URL').pack()
e = Entry(root, borderwidth = 5, width = 60)
e.pack()


radio_var = IntVar()

Radiobutton(root, text='Download as video (mp4)', variable=radio_var, value=1).pack()
Radiobutton(root, text='Download as audio (mp3)', variable=radio_var, value=2).pack()

lblSpace = Label(root, text='\n').pack()

btnDownload = Button(root, text='Download!', borderwidth = 5 ,command=lambda: download(radio_var.get(), e.get())).pack()

lblObs = Label(root, text='\n \n Do not close the program until a new window appears, with an error or success message', fg='red').pack()
root.mainloop()
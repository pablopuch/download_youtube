from pytube import YouTube
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip
from tkinter import *
import shutil


def accion():
    enlace = videos.get()
    video = YouTube(enlace)
    descarga = video.streams.get_highest_resolution().download()
     
def url_dowload():
     path = filedialog.askdirectory()
     boton_url.config(text=path, fg='blue')
    
def popup():
    messagebox.showinfo('Sobre mi','https://www.linkedin.com/in/pablopuch/')

root = Tk()
root.config(bd=15)
root.title('Script descargar Vídeos')


imagen = PhotoImage(file='resources/Youtube_logo.png')
new_img = imagen.subsample(3,3)

foto = Label(root, image=new_img, bd=0)
foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label='Para más información', menu=helpmenu)
helpmenu.add_command(label='Información del autor', command=popup)
menubar.add_command(label='Salir', command=root.destroy)

instrucciones = Label(root, text='Programa creado en Python para descargar vídeos de Youtube\n')
instrucciones.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

boton_url = Button(root, text='Url de descarga', command=url_dowload)
boton_url.grid(row=3, column=1)

boton = Button(root, text='Descargar', command=accion)
boton.grid(row=2, column=1)

alert = Label(root, text='')

root.mainloop()
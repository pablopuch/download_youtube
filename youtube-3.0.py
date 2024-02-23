from pytube import YouTube, Playlist
from tkinter import filedialog, messagebox
from pydub import AudioSegment
from tkinter import *
import os

def accion():
    enlace = videos.get()

    try:
        # Intenta crear una instancia de Playlist
        playlist = Playlist(enlace)

        # Itera sobre los vídeos en la lista de reproducción
        for video in playlist.videos:
            descargar_audio(video)

        # Muestra un mensaje de éxito cuando se completa la descarga
        messagebox.showinfo('Éxito', f'Toda la lista de reproducción se descargó y convirtió a MP3 correctamente.')

    except Exception as e:
        # Muestra un mensaje de error si algo sale mal
        messagebox.showerror('Error', f'Error al descargar la lista de reproducción: {str(e)}')

def descargar_audio(video):
    # Obtiene la mejor pista de audio disponible
    audio_stream = video.streams.filter(only_audio=True).first()

    # Descarga la pista de audio en formato webm
    descarga = audio_stream.download()

    # Ruta de destino para el archivo de audio (mp3)
    audio_path = os.path.splitext(descarga)[0] + ".mp3"

    try:
        # Convierte el archivo de audio a formato mp3 usando pydub
        audio = AudioSegment.from_file(descarga)
        audio.export(audio_path, format="mp3")

    except Exception as e:
        # Muestra un mensaje de error si algo sale mal
        messagebox.showerror('Error', f'Error al convertir a MP3: {str(e)}')

    # Elimina el archivo de audio original en formato webm
    os.remove(descarga)

def url_dowload():
    path = filedialog.askdirectory()
    boton_url.config(text=path, fg='blue')

def popup():
    messagebox.showinfo('Sobre mí', 'https://www.linkedin.com/in/pablopuch/')

root = Tk()
root.config(bd=15)
root.title('Script descargar Lista de Reproducción')

imagen = PhotoImage(file='resources/Youtube_logo.png')
new_img = imagen.subsample(3, 3)

foto = Label(root, image=new_img, bd=0)
foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label='Para más información', menu=helpmenu)
helpmenu.add_command(label='Información del autor', command=popup)
menubar.add_command(label='Salir', command=root.destroy)

instrucciones = Label(root, text='Programa creado en Python para descargar listas de reproducción de Youtube\n')
instrucciones.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

boton_url = Button(root, text='Url de descarga', command=url_dowload)
boton_url.grid(row=3, column=1)

boton = Button(root, text='Descargar Lista de Reproducción', command=accion)
boton.grid(row=2, column=1)

alert = Label(root, text='')

root.mainloop()

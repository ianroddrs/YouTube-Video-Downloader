from tkinter import *
from pytube import YouTube


def baixar_video():
    # Label(janela, text='FAZENDO DOWNLOAD...', background='#1C1C1C', foreground='#FFF', font=('Helvetica', 18, 'bold'), anchor=W).place(x=110, y=400, width=500, height=20)

    video = YouTube(url.get())
    video.streams.get_highest_resolution().download(output_path='C:/YTD-DOWNLOADS')  # + save.get())

    Label(janela, text='DOWNLOAD CONCLUÍDO COM SUCESSO', background='#1C1C1C', foreground='#00ff00',
          font=('Helvetica', 14, 'bold'), anchor=N).place(x=110, y=380, width=500, height=60)
    Label(janela, text='Salvo em: C:/YTD-DOWNLOADS', background='#1C1C1C', foreground='#FFF',
          font=('Helvetica', 11, 'bold'), anchor=N).place(x=110, y=410, width=500, height=60)


janela = Tk()
janela.title('YouTube Downloader by @IanRoddrs')
janela.geometry('720x500')
janela.configure(background='#1C1C1C')

Label(janela, text='YouTube URL:', background='#1C1C1C', foreground='#FFF', font=('Helvetica', 18, 'bold'),
        anchor=W).place(x=110, y=150, width=500, height=20)
url = Entry(janela, background='#000', foreground='#FFF', font=('Helvetica', 15, 'bold'), border=0)
url.place(x=110, y=180, width=500, height=70)

btn = Button(janela, text='Download', background='#800000', foreground='#FFF', font=('Helvetica', 18, 'bold'),
        cursor='hand2', border=0, command=baixar_video)
btn.place(x=110, y=260, width=500, height=70)

janela.mainloop()

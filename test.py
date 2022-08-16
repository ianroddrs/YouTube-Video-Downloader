from pytube import YouTube

url = input(str('Url para download: '))
caminho = input(str('salvar em: '))

#BAIXAR VÍDEO
print('BAIXANDO VIDEO...')
video = YouTube(url)
video.streams.get_highest_resolution().download(output_path='C:/' + caminho)

#BAIXAR MP3
print('BAIXANDO AUDIO...')
musica = YouTube(url)
musica.streams.filter(only_audio=True).first().download(output_path='C:/' + caminho, filename=musica.title + '.mp3')

print('DOWNLOAD CONCLUÍDO COM SUCESSO!')

#
# pip install pyinstaller
# pyinstaller --version
# pyinstaller --onefile --noconsole .\name
#

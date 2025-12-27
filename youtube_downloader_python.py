
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix import exceptions
import os

def youtube_video_download(url: str, path: str):
    try:
        yt = YouTube(url, on_progress_callback = on_progress)
        print(yt.title)
        ys = yt.streams.get_highest_resolution()
        ys.download(output_path=path)
        print("\nDone")
    except exceptions.VideoUnavailable:
        print("Try a different URL...")
        

def youtube_audio_download(url: str, base: str):
    try:
        yt = YouTube(url, on_progress_callback = on_progress)
        print(yt.title)
        ys = yt.streams.filter(only_audio=True).first()
        out_file = ys.download(output_path='.')
        new_file = f'{base}\{yt.title}.mp3'
        print(new_file)
        os.rename(out_file, new_file)
        print("\nDone!")
    except FileExistsError:
        print(f'File already exist. {base}')

def main():
       
    url = input('Enter url: ')
    # path = input('Which do you want this file saved: ')
    base = input('Where to save audio file to: ')

    youtube_audio_download(url, base)

if __name__ == "__main__":

    main()


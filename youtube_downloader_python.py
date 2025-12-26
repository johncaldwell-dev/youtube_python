
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix import exceptions
import os

def youtube_video_download(url, path):
    try:
        yt = YouTube(url, on_progress_callback = on_progress)
        print(yt.title)
        ys = yt.streams.get_highest_resolution()
        ys.download(output_path=path)
        print("\nDone")
    except exceptions.VideoUnavailable:
        print("Try a different URL...")
        main()

def youtube_audio_download():
    url = ""
    yt = YouTube(url, on_progress_callback = on_progress)
    print(yt.title)
    ys = yt.streams.filter(only_audio=True).first()
    out_file = ys.download(output_path='.')
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print("\nDone!")

def main():
       
    url = input('Enter url: ')
    path = input('Which do you want this file saved: ')

    youtube_video_download(url, path)

if __name__ == "__main__":

    main()


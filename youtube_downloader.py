
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix import exceptions
import os
from pytubefix import YouTube

def select_video_or_audio(selection, url, path, progress_bar, progress_label):
    def on_progress(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percent = bytes_downloaded / total_size

        progress_bar.set(percent)
        progress_label.configure(text=f"Progress: {int(percent * 100)}%")

    yt = YouTube(url, on_progress_callback=on_progress)

    if selection == "video":
        stream = yt.streams.get_highest_resolution()
    else:
        stream = yt.streams.filter(only_audio=True).first()

    stream.download(output_path=path)

    progress_label.configure(text="Download complete!")

def main():

    raise NotImplementedError

    

if __name__ == "__main__":

    main()


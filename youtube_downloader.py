import os
import re
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix import exceptions
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
        stream.download(output_path=path)
    else:
        stream = yt.streams.filter(only_audio=True).first()
        out_file = stream.download(output_path='.')

        # Remove invalid filename characters
        safe_title = re.sub(r'[\\/*?:"<>|]', "", yt.title)

        new_file = os.path.join(path, f"{safe_title}.mp3")
        os.rename(out_file, new_file)
    
    

    progress_label.configure(text="Download complete!")

def main():

    raise NotImplementedError

    

if __name__ == "__main__":

    main()


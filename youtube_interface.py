import customtkinter
import youtube_downloader

resolution = "600x350"

window = customtkinter.CTk()
window.geometry(resolution)
font_title = customtkinter.CTkFont(family="Comic Sans MS", size=30)

customtkinter.CTkLabel(
    window,
    text="YouTube Downloader",
    font=font_title,
    text_color="red"
).place(x=180, y=15)

customtkinter.CTkLabel(window, text="Enter the YouTube URL: ").place(x=20, y=100)
txtyoutube_url = customtkinter.CTkEntry(window, width=380, height=25)
txtyoutube_url.place(x=160, y=100)

customtkinter.CTkLabel(window, text="Where to save video or audio: ").place(x=20, y=150)
txtsave_location = customtkinter.CTkEntry(window, width=350, height=25)
txtsave_location.place(x=190, y=150)

customtkinter.CTkLabel(window, text="How do you want to save the download: ").place(x=20, y=200)

cboselection = customtkinter.CTkComboBox(
    window,
    values=["Video", "Audio"]
)
cboselection.set("Video")  # 👈 default selection
cboselection.place(x=50, y=250)

progress_label = customtkinter.CTkLabel(window, text="Progress: 0%")
progress_label.place(x=50, y=280)

progress_bar = customtkinter.CTkProgressBar(window, width=500)
progress_bar.set(0)
progress_bar.place(x=50, y=305)


def download():
    selection = cboselection.get().lower()
    youtube_url = txtyoutube_url.get()
    save_location = txtsave_location.get()

    youtube_downloader.select_video_or_audio(
        selection,
        youtube_url,
        save_location,
        progress_bar,
        progress_label
    )

    txtyoutube_url.delete(0, customtkinter.END)
    txtsave_location.delete(0, customtkinter.END)

btndownload = customtkinter.CTkButton(
    window,
    text="Download Now",
    command=download
)
btndownload.place(x=300, y=225)

window.mainloop()
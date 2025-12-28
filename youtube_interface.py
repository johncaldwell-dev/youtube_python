import customtkinter
import youtube_downloader

resolution = "600x400"

window = customtkinter.CTk()
window.geometry(resolution)
font_title = customtkinter.CTkFont(family="Comic Sans MS", size=30)

customtkinter.CTkLabel(window, text="YouTube Downloader", font=font_title, text_color="red").place(x=180, y=15)

customtkinter.CTkLabel(window, text="Enter the YouTube URL: ").place(x=20, y=100)
youtube_url = customtkinter.CTkEntry(window, width=380, height=25)
youtube_url.place(x=160, y=100)

customtkinter.CTkLabel(window, text="Where to save video or audio: ").place(x=20, y=150)
save_location = customtkinter.CTkEntry(window, width=350, height=25)
save_location.place(x=190, y=150)

window.mainloop()
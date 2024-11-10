import customtkinter as ctk
from tkinter import filedialog
import moviepy.editor as mp

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Video to Audio Converter")
app.geometry("400x300")

def select_video():
    file_path = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")]
    )
    video_path_entry.delete(0, ctk.END)
    video_path_entry.insert(0, file_path)

def extract_audio():
    video_path = video_path_entry.get()
    output_name = output_name_entry.get()

    if video_path and output_name:
        try:
            cvt_video = mp.VideoFileClip(video_path)
            ext_audio = cvt_video.audio
            ext_audio.write_audiofile(f"{output_name}.mp3")
            status_label.config(text="Audio extracted successfully!", text_color="green")
        except Exception as e:
            status_label.config(text=f"Error: {str(e)}", text_color="red")
    else:
        status_label.config(text="Please enter both the video path and output name.", text_color="red")

video_path_label = ctk.CTkLabel(app, text="Video Path:")
video_path_label.pack(pady=10)

video_path_entry = ctk.CTkEntry(app, width=300)
video_path_entry.pack()

browse_button = ctk.CTkButton(app, text="Browse", command=select_video)
browse_button.pack(pady=5)

output_name_label = ctk.CTkLabel(app, text="Output Audio File Name:")
output_name_label.pack(pady=10)

output_name_entry = ctk.CTkEntry(app, width=300)
output_name_entry.pack()

convert_button = ctk.CTkButton(app, text="Convert to Audio", command=extract_audio)
convert_button.pack(pady=20)

status_label = ctk.CTkLabel(app, text="")
status_label.pack(pady=10)

app.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox
from yt_dlp import YoutubeDL

# Fungsi untuk mendownload video
def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Masukkan URL video YouTube!")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
    if not save_path:
        return

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': save_path,  # Menggunakan path yang dipilih pengguna
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            print(f"Judul: {info_dict['title']}")
            print(f"Thumbnail URL: {info_dict['thumbnail']}")

            print("Sedang mendownload...")
            ydl.download([url])
            print("Download selesai!")
            messagebox.showinfo("Sukses", "Video berhasil didownload!")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

# Membuat GUI
app = tk.Tk()
app.title("YouTube Video Downloader")

# Label dan Entry untuk URL
tk.Label(app, text="Masukkan URL YouTube:").pack(pady=5)
url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=5)

# Tombol untuk memilih lokasi penyimpanan dan mendownload
tk.Button(app, text="Pilih Lokasi Simpan & Download", command=download_video).pack(pady=20)

# Menjalankan aplikasi
app.mainloop()
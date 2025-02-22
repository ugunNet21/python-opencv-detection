from yt_dlp import YoutubeDL

# URL video YouTube
url = "https://www.youtube.com/watch?v=0CyxgLbS_1I"

# Konfigurasi download
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # Format terbaik (mp4)
    'outtmpl': '%(title)s.%(ext)s',  # Nama file output
}

# Membuat objek YoutubeDL
with YoutubeDL(ydl_opts) as ydl:
    # Mendapatkan informasi video
    info_dict = ydl.extract_info(url, download=False)
    print(f"Judul: {info_dict['title']}")
    print(f"Thumbnail URL: {info_dict['thumbnail']}")

    # Mendownload video
    print("Sedang mendownload...")
    ydl.download([url])
    print("Download selesai!")
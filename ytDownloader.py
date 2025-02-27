import os
import yt_dlp

# İndirme klasörünü kontrol eden ve yoksa oluşturan fonksiyon
def check_download_folder():
    download_path = os.path.join(os.getcwd(), "downloads")
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    return download_path

# Youtube videosunu indiren fonksiyon
def Download(link):
    try:
        download_path = check_download_folder()  # Klasör kontrolü
        ydl_opts = {
            "format": "best",
            "outtmpl": os.path.join(download_path, "%(title)s.%(ext)s"),
            "quiet": False
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=True)
            print(f"İndirme Tamamlandı: {info.get('title', 'Bilinmeyen Başlık')}")
    except Exception as e:
        print(f"İndirme Başarısız ({link}): {str(e)}")

# Kullanıcıdan kaç link gireceğini al
while True:
    try:
        link_count = int(input("Kaç link gireceksiniz? : "))
        if link_count <= 0:
            print("Lütfen pozitif bir sayı girin.")
            continue
        break
    except ValueError:
        print("Geçerli bir sayı girin.")

# Kullanıcıdan linkleri al ve her birini indir
for _ in range(link_count):
    link = input("Link : ")
    Download(link)

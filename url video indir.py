
import os
import time
import pytube
from moviepy.editor import VideoFileClip

def video_indir(url, hedef_dosya, mp3_olarak=False):
    try:
        youtube = pytube.YouTube(url)
        video = youtube.streams.filter(file_extension='mp4').first()

        # Videoyu belirtilen dosya adına indir
        video.download(filename=hedef_dosya)

        if mp3_olarak and hedef_dosya.endswith('.mp4'):
            # Dosya adı .mp4 uzantılıysa ve mp3_olarak seçeneği işaretlenmişse dönüştür
            mp4_file = hedef_dosya
            mp3_file = hedef_dosya[:-4] + '.mp3'  # .mp4 uzantısını .mp3 ile değiştir
            clip = VideoFileClip(mp4_file)
            clip.audio.write_audiofile(mp3_file)
            clip.close()
            os.remove(mp4_file)
            print(f"{hedef_dosya} dosyası başarıyla mp3 formatına dönüştürüldü: {mp3_file}")
        else:
            print(f"{hedef_dosya} dosyası başarıyla indirildi.")

    except pytube.exceptions.RegexMatchError:
        print("Hata oluştu: URL geçersiz.")
    except pytube.exceptions.VideoUnavailable:
        print("Hata oluştu: Video kullanılamıyor.")
    except Exception as e:
        print(f"Hata oluştu: {str(e)}")

# Video indirme örneği
print("- Çıkış için 'Q' basınız.")
while True:
    video_url = input("YouTube Video URL'sini yazınız: ")
    if video_url.lower() == "q":
        print("- Çıkış yapılıyor..")
        time.sleep(3)
        break
    hedef_dosya = input("Hedef dosyanın adını yazınız (.mp4 veya .mp3 uzantısını ekleyin): ")
    if hedef_dosya.lower() == "q":
        print("- Çıkış yapılıyor..")
        time.sleep(3)
        break
    
    if hedef_dosya.endswith('.mp3'):
        video_indir(video_url, hedef_dosya, mp3_olarak=True)
    else:
        video_indir(video_url, hedef_dosya)
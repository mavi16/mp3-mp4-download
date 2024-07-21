# YouTube Video İndirici ve MP3 Dönüştürücü

Bu Python projesi, YouTube videolarını `.mp4` formatında indirmenizi ve isteğe bağlı olarak bu videoları `.mp3` formatına dönüştürmenizi sağlar. `pytube` kütüphanesini video indirmek için, `moviepy` kütüphanesini ise video dosyalarını ses dosyasına dönüştürmek için kullanır.

## Özellikler

- YouTube videolarını `.mp4` formatında indirir.
- Videoları isteğe bağlı olarak `.mp3` formatına dönüştürür.
- Kullanıcı dostu komut satırı arayüzü.

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız olacak:

- `pytube`: YouTube videolarını indirmek için
- `moviepy`: Videoları mp3 formatına dönüştürmek için

Bu kütüphaneleri yüklemek için aşağıdaki komutu kullanabilirsiniz:
```bash
pip install pytube moviepy
```

## Hata Yönetimi
URL geçersiz: Hatalı bir YouTube URL'si girildiğinde, "Hata oluştu: URL geçersiz." mesajı gösterilir.
Video kullanılamıyor: Video mevcut değilse veya erişilemiyorsa, "Hata oluştu: Video kullanılamıyor." mesajı gösterilir.
Diğer hatalar: Genel hatalar yakalanır ve hata mesajı olarak gösterilir.

## Katkıda Bulunanlar
BARAN - Proje sahibi ve geliştirici

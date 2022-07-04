from yt_dlp import YoutubeDL
my_url = str(input('링크 입력: '))
ydl_opt = {'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'}
URLS = [my_url]
with YoutubeDL(ydl_opt) as ydl:
    ydl.download(URLS)
print('다운로드 완료')

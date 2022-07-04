import youtube_dl
my_url = str(input('링크 입력: '))
ydl_opt = {'format': 'bestvideo/best'}
with youtube_dl.YoutubeDL(ydl_opt) as ydl:
    ydl.download([my_url])
print('다운로드 완료')

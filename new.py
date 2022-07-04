from yt_dlp import YoutubeDL

my_url = str(input('링크 입력: '))

ydl_opt = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }, {'key': 'FFmpegMetadata'}, ],
}

URLS = [my_url]
with YoutubeDL(ydl_opt) as ydl:
    ydl.download(URLS)

print('다운로드 완료')

#import os
import youtube_dl

#output_dir = os.path.join('./', '%(playlist_title)s', '%(playlist_index)s. %(title)s.%(ext)s')

my_url = str(input('링크 입력: '))

ydl_opt = {
    #'outtmpl': output_dir,
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }, {'key': 'FFmpegMetadata'},], # 메타데이터도 함께 저장
}

with youtube_dl.YoutubeDL(ydl_opt) as ydl:
    ydl.download([my_url])

print('다운로드 완료')

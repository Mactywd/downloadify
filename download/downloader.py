from __future__ import unicode_literals
import youtube_dl


class MyLogger(object):
    def __init__(self, idx, total):
        self.idx = idx
        self.total = total

    def debug(self, msg):
        print(msg, f'  {self.idx+1}/{self.total}')

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

def download(url, track_idx, total, sp_title):
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'files/{}.%(ext)s'.format(sp_title),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': MyLogger(track_idx, total),
        'progress_hooks': [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    print("Downloaded: " + ydl_opts["outtmpl"].split('/')[1])

if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=h6elJiioKt4'

    download(url, 0, 0)
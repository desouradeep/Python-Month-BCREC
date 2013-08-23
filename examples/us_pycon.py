from requests import get
from feedparser import parse
from urllib import urlretrieve
from os import system

req = get('http://pyvideo.org/category/33/pycon-us-2013/rss')
dic = parse(req.text)
for entry in dic['entries']:
    try:
        video_link = entry.links[1]['href']
        print 'Downloading video', video_link
        if video_link.startswith('https://www.youtube.com'):
            download_link = 'youtube-dl -o "%(title)s.%(ext)s" --restrict-filenames '+ video_link
            system(download_link)
        else:
            download_link = video_link
            file_name = video_link[52:video_link.find('?')]
            urlretrieve(download_link, file_name)
    except:
        pass
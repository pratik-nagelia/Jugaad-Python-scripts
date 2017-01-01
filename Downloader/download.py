import requests
from bs4 import BeautifulSoup
import urllib
url = "https://gre.magoosh.com/sessions"
next_lesson = "https://gre.magoosh.com/lessons/996-general-introduction"
count = 1
payload = {
    'authenticity_token' : 'gA1u6AFndliuFEYxP0wLUvqeU9oCZK/HfajAb5DNANs=',
    'session[login]' :'', #Enter Username
    'session[password]' : '', #Enter Password
    'commit':'Sign In'
}

def gen_filename(title):
    filename = "/home/patrick/gre/"+str(count)+". "+title+".mp4"
    return filename

def download_video(video_url, filename):
    urllib.URLopener().retrieve(video_url, filename)


with requests.Session() as s:
    p = s.post(url, data=payload)
    while count < 5100:
        page = s.get(next_lesson)
        soup = BeautifulSoup(page.text, "html.parser")
        title = soup.title.text.strip()
        try:
            video_url = soup.find('div', {'class': 'video_container '})['data-file']
            print video_url
            filename = gen_filename(title)
            download_video(video_url, filename)
            print filename
            count +=1
        except:
            print "video downloading failed : "+next_lesson
        next_lesson = "https://gre.magoosh.com/" + soup.find('ul', {'id': 'next_lesson'}).li.a['href']
from twilio.rest import TwilioRestClient
import requests
from bs4 import BeautifulSoup
import urllib2
import time
import cookielib
import sys
import socket

needle = 'loot'
urll = "http://www.indiafreestuff.in/forum/forum/5-hotdeals-forum/"  # ?page="+str(pgno)
last = ''
jession_id = ' '
number = "8084033193"  # raw_input("Enter Mobile number:")

ACCOUNT_SID = 'ACef3a41999c12d31b09d595effb578b7'
AUTH_TOKEN = '3856662e953ce4d63b790634d58fa66'
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

def sendSMS(message):
    client.messages.create(
        to='+919430767502',
        from_='+13343103023',
        body=message,
    )
maxx = 0
while True:
    try:
        source_code = requests.get(urll)
    except requests.ConnectionError, e:
        time.sleep(30)
        continue
    except socket.error as e:
        time.sleep(30)
        continue
    html_text = source_code.text
    soup = BeautifulSoup(html_text, "html.parser")
    posts = soup.findAll(itemtype="http://schema.org/Article")
    pre = maxx
    print str(posts)
    for post in posts:
        id = int(post['data-rowid'])
        title = post.find('span', attrs={'itemprop':'name headline'}).text.strip().encode('utf8')
        print (title)
        if id <= pre:
            continue
        if needle in title.lower():
            print "loot found : "+title
            sendSMS(title)
        maxx = max(maxx, id)
    time.sleep(200)

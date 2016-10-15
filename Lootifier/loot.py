import random
import requests
from bs4 import BeautifulSoup
import urllib2
import time
import cookielib
from getpass import getpass
import sys
import socket

needle = 'loot'
urll = "http://www.indiafreestuff.in/forum/forum/5-hotdeals-forum/"  # ?page="+str(pgno)
last = ''
jession_id = ' '
username = "8084033193"  # raw_input("Enter Username: ")
passwd = "1325"  # getpass()
number = "8084033193"  # raw_input("Enter Mobile number:")
url = 'http://site24.way2sms.com/Login1.action?'
data = 'username=' + username + '&password=' + passwd + '&Submit=Sign+in'
maxx = 0
# For Cookies:
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

# Adding Header detail:
opener.addheaders = [('User-Agent',
                      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]


def login():
    global usock
    try:
        usock = opener.open(url, data)
    except IOError:
        print ("Error while logging in")
        sys.exit(1)
    global jession_id
    jession_id = str(cj).split('~')[1].split(' ')[0]


def sendSMS(message):
    login()
    message = "+".join(message.split(' '))

    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token=' + jession_id + '&mobile=' + number + '&message=' + message + '&msgLen=136'
    opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token=' + jession_id)]

    try:
        sms_sent_page = opener.open(send_sms_url, send_sms_data)
    except IOError:
        print ("Error while sending message")
        time.sleep(10)
        sms_sent_page = opener.open(send_sms_url, send_sms_data)
    # sys.exit(1)
    print ("SMS has been sent.")
    time.sleep(5)


while True:
    try:
        source_code = requests.get(urll)
    except requests.ConnectionError, e:
        time.sleep(10)
        continue
    except socket.error as e:
        time.sleep(10)
        continue
    html_text = source_code.text
    # print(html_text)
    soup = BeautifulSoup(html_text, "html.parser")
    posts = soup.findAll(itemtype="http://schema.org/Article")
    print str(posts)
    for post in posts:
        pre = maxx
        id = int(post['data-rowid'])
        title = post.span.text.strip().encode('utf8')
        print title
        if id == pre and title != '':
            break
        if needle in title.lower():
            # print (line)
            print "loot found :"
            sendSMS(title)
        maxx = max(maxx, id)
    #print (title.encode('utf8'))
    time.sleep(200)

from twilio.rest import TwilioRestClient
import requests
from bs4 import BeautifulSoup
import urllib2
import time
import cookielib
import sys
import socket

link = "https://www.codechef.com/rankings/ACMIND16/sites"
source_code = requests.get(link)
html_text = source_code.text
soup = BeautifulSoup(html_text, "html.parser")
posts = soup.findAll('')
print posts

number = "9430767502"  # raw_input("Enter Mobile number:")

ACCOUNT_SID = 'ACef3a41999c12d31b09d595effb578b75'
AUTH_TOKEN = '3856662e953ce4d63b790634d58fa664'
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)


def sendSMS(message):
    client.messages.create(
        to='+919430767502',
        from_='+13343103023',
        body=message,
    )
sendSMS("yooooooo")
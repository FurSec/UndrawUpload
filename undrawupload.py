import base64
import sys
import requests
import random

def upload(image):
	with open('useragents.txt', 'r') as u:
		useragent = random.choice(u.read().splitlines())
	headers = {'user-agent':useragent}
	payload = {'image':image}
	r = requests.post('http://wtf.undraw.it/inc/send.php', headers=headers, data=payload)
	print r.text

def main():
	image = sys.argv[1]
	with open(image, 'rb') as r:
		encoded_image = base64.encodestring(r.read())
	upload(encoded_image)

if __name__ == '__main__':
	main()

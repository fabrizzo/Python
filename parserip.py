import requests
from bs4 import BeautifulSoup
import re
from random import choice
from time import sleep
from random import uniform

def get_html(url, useragent=None, proxy=None):
	r = requests.get(url, headers=useragent, proxies=proxy)
	return r.text

def get_ip(html):
	print('New Proxy & User-Agent:')
	soup = BeautifulSoup(html,'lxml')
	ip = soup.find('form', action='./').find('input').get('value')
	ua = soup.find(text=re.compile('browser'))
	ua = ua.split("Agent:")[1]
	print(ip)
	print(ua)
	print ('-----------------------')


def main():

	url = 'http://atomurl.net/myip/'
	useragents = open('UA.txt').read().split('\n')
	proxi = open('proxylist.txt').read().split('\n')

	for i in range(4):
		a= uniform(3,6)
		sleep(a)
		try:
			proxy = {'http':'http://' + choice(proxi)}
		except:
			proxy - ''
		try:
			useragent = {'User-Agent': choice(useragents)}
		except:
			useragent = ''	
		html = get_html(url, useragent, proxy)
		get_ip(html)


if __name__ == '__main__':
	main()
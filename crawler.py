import requests

from bs4 import BeautifulSoup

import csv
from datetime import datetime

from multiprocessing import Pool


def get_html(url):
	r = requests.get(url) #Response
	return r.text

def get_all_links(html):
	soup = BeautifulSoup(html, 'lxml')

	tds = soup.find('table', class_='catalog_table').find_all('td', class_='item-name')


	links = []

	for td in tds:
		a = td.find('a').get('href')
		link = 'https://mebelkom.com' + a
		links.append(link)


	return links


def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')
	try:
		name = soup.find('h1').text.strip()
	except:
		name = ''
	try:
		price = soup.find('span', class_='price ib').text.strip()
	except:
		price = ''
	data = {'name' : name,
			'price': price}
	return data



def write_csv(data):
	with open('mebelkomplect.csv', 'a') as f:
		writer = csv.writer(f)

		writer.writerow( (data['name'],
						  data['price']) )

		print (data['name'], data['price'], 'parsed')


def make_all(url):
	html = get_html(url)
	data = get_page_data(html)
	write_csv(data)


def main():


	start = datetime.now()
	url = 'https://mebelkom.com/catalog/ldsp/?show=all'

	all_links = get_all_links( get_html(url) )
	
	#for url in all_links:
	#	html = get_html(url)
	#	data = get_page_data(html)
	#	write_csv(data)

	with Pool(2) as p:
		p.map(make_all, all_links)









	end = datetime.now()

	total = end - start
	print(str(total))

if __name__ == '__main__':
	main()
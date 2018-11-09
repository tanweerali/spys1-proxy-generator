import requests
from bs4 import BeautifulSoup
import sys


first_arg = sys.argv[1]



def get_proxy(first_arg):

	proxy_url = 'https://pastebin.com/u/spys1'

	page_soup = []

	r = requests.get(proxy_url)
	html_content = r.text
	page_soup.append(BeautifulSoup(html_content,"html.parser"))


	for i in page_soup:
		link = (i.td.a['href'])

	pastebin_url = 'https://pastebin.com'+link
	###
	page_soup = []

	r = requests.get(pastebin_url)
	html_content = r.text
	page_soup.append(BeautifulSoup(html_content,"html.parser"))
	###
	proxy = []

	for s in page_soup:
		for i in s.find_all('div',class_='de1'):
			proxies = i.text
			proxy.append(proxies)

		Proxy = []

		for p in proxy[1:]:
			if first_arg in p:
				proxies = p.rsplit(' ',-1)[0].replace(' ','')
				Proxy.append(proxies)

		print(Proxy)




if __name__ == "__main__":
		get_proxy(first_arg)

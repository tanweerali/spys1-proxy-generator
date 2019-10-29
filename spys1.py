import requests
from bs4 import BeautifulSoup
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--country", required=True, 
                help="proxy origin country")
args = vars(ap.parse_args())

first_arg = args['country'].upper()

class Proxy_Generate():
    
    def proxy_soup():

        proxy_url = 'https://pastebin.com/u/spys1'

        page_soup = []

        r = requests.get(proxy_url)
        html_content = r.text
        page_soup.append(BeautifulSoup(html_content,"html.parser"))

        for i in page_soup:
            link = (i.td.a['href'])

        pastebin_url = 'https://pastebin.com'+link

        page_soup = []

        r = requests.get(pastebin_url)
        html_content = r.text
        page_soup.append(BeautifulSoup(html_content,"html.parser"))

        proxy = []

        for s in page_soup:
            for i in s.find_all('div',class_='de1'):
                proxies = i.text
                proxy.append(proxies)
        return proxy
    
    
    def get_proxy(first_arg, proxy_soup = proxy_soup()):
        proxy = proxy_soup
        country = first_arg
        for p in proxy[1:]:
            if country in p:
                proxies = p.rsplit(' ',-1)[0].replace(' ','')                
                print(proxies)       



if __name__ == "__main__":
    Proxy_Generate.get_proxy(first_arg)

import urllib2
from bs4 import BeautifulSoup as soup

base_url = 'https://coinmarketcap.com/currencies/'

def cointhings():
 with open('coins', 'r') as text:
  for line in text:
    url = base_url + line
    page = urllib2.urlopen(url)
    bsoup = soup(page, 'html.parser')
    titlecoin=bsoup.find('small', {'class': 'bold hidden-sm hidden-md hidden-lg'})
    print titlecoin.text
    pricecoin=bsoup.find('span', {'class': 'text-large2'})
    print pricecoin.text

cointhings()


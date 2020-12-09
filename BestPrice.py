import requests
from bs4 import BeautifulSoup

def trade_spider(urls):
 for url in urls:
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for h1 in soup.findAll('h1', {'class': 'category-title'}):
        name = h1.string
        print(name)
    count = 0
    for div in soup.findAll('div', {'class': 'price'}):
        count = count+1
        best_price = div.string
        if(count == 1):
         print(best_price)
    most_expensive(url)
    for span in soup.findAll('span', {'class': 'product-num visible-xs-inline-block visible-sm-inline-block'}):
        for span2 in span.find_all('span'):
         print(span2.string)

def most_expensive(url):
    new_url = url + "?orderby=2"
    source_code = requests.get(new_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    count = 0
    for div in soup.findAll('div', {'class': 'price'}):
        count = count + 1
        most_expensive = div.string
        if (count == 1):
            print(most_expensive)

urls = ['https://www.compari.ro/monitoare-c3126/', 'https://incarcator-auto.compari.ro/', 'https://www.compari.ro/masini-de-spalat-c3167/']
trade_spider(urls)
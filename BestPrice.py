import requests
import json
import re
from bs4 import BeautifulSoup
product_iformations = []
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
         break
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
            break
    for span in soup.findAll('span', {'class': 'product-num visible-xs-inline-block visible-sm-inline-block'}):
        for span2 in span.find_all('span'):
            number = span2.string
            number = re.split('\s', number)[0]
            print(number)
    product_iformations.append({"name": name.strip(),
                                "best price": best_price,
                                "most expensive": most_expensive,
                                "number of products":int(number)})
    with open("products_json_detail.json", "w") as prod:
        json.dump(product_iformations, prod)

urls = ['https://www.compari.ro/monitoare-c3126/', 'https://incarcator-auto.compari.ro/', 'https://www.compari.ro/masini-de-spalat-c3167/']
trade_spider(urls)
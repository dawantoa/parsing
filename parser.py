import requests
from bs4 import BeautifulSoup
URL = 'https://auto.ria.com/legkovie/jeep/'
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
HOST = 'https://auto.ria.com'
def get_html(url,params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('section',class_='ticket-item')
    cars = []
    for item in items:
        cars.append({
            'title': item.find('a', class_='address').get_text(strip=True),
            'link': item.find('a', class_='address').get('href'),
            'usd_price': item.find('span', class_='bold green size22').get_text(),
        })
    return  cars


def parse():
    html = get_html(URL)
    print(html)
    if html.status_code == 200:
        cars = get_content(html.text)
    else:
        print('Error')

parse()
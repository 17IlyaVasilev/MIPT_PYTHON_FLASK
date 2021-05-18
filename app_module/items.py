from urllib.request import urlopen
from bs4 import BeautifulSoup


tp = []
tp1 = []
st = ''
url_to_scrape = "https://smart-lab.ru/q/shares/"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

items = html_soup.find_all('tr')

for item in items:
    temp = item.find_all('td')
    if (len(temp) > 10):
        title = temp[3].text
        price = temp[7].text
        if (len(title) > 0 and len(price) > 0):
            tp.append(title)
            tp1.append(price)
            st += title + '\n'

cur = tp[0] + ' ' + tp1[0]
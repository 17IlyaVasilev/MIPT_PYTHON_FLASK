from app_module import app
from flask import render_template, url_for
from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import request
from app_module import items as it



@app.route('/')
def home():
    it.url_to_scrape = "https://smart-lab.ru/q/shares/"
    it.tp.clear()
    it.tp1.clear()
    it.st = ''
    it.request_page = urlopen(it.url_to_scrape)
    it.page_html = it.request_page.read()
    it.request_page.close()
    it.html_soup = BeautifulSoup(it.page_html, 'html.parser')
    it.items = it.html_soup.find_all('tr')

    for item in it.items:
        temp = item.find_all('td')
        if (len(temp) > 10):
            title = temp[3].text
            price = temp[7].text
            if (len(title) > 0 and len(price) > 0):
                it.tp.append(title)
                it.tp1.append(price)
                it.st += title + '\n'

    return render_template("home.html", n = it.cur, s = it.st)


@app.route('/search')
def search():
    title = request.args.get("title")
    price = ""
    for i in range(len(it.tp)):
        if (it.tp[i] == title):
            cur = n = title + ' ' + it.tp1[i]
            return render_template("home.html", n = title + ' ' + it.tp1[i], s = it.st)
    return render_template("home.html", n = "No such ticker of stock. You can try to find correct ticker", s = it.st)

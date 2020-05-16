import requests
from bs4 import BeautifulSoup
import csv

def quote_scraper():
    url = "http://quotes.toscrape.com"
    quote_list = []
    next_link = url

    while True:
        response = requests.get(next_link)
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_ = "quote")
        for quote in quotes:
            text = quote.find("span", class_ = "text").text
            print(text)

        next_page = soup.find("li", class_ = "next")
        
        if next_page:
            next_path = next_page.find("a")["href"]
            next_link = url + next_path
            print(next_link)
        else:
            break
        #nothing


quote_scraper()
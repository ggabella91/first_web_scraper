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
            author = quote.find("small", class_ = "author").text
            author_bio_path = quote.find("a")["href"]
            #print(author_bio_path)
            bio = get_author_bio(author_bio_path)
            
            text = quote.find("span", class_ = "text").text
            #print(text)

        next_page = soup.find("li", class_ = "next")
        
        if next_page:
            next_path = next_page.find("a")["href"]
            next_link = url + next_path
            print(next_link)
        else:
            break

def get_author_bio(path):
    url = "http://quotes.toscrape.com"
    response = requests.get(url+path)
    soup = BeautifulSoup(response.text, "html.parser")
    born_date = soup.find("span", class_ = "author-born-date").text 
    born_location = soup.find("span", class_ = "author-born-location").text
    bio = born_date + " " + born_location
    return bio


quote_scraper()
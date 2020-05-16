import requests
from bs4 import BeautifulSoup
import csv
from random import choice

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
            bio_path = quote.find("a")["href"]
            text = quote.find("span", class_ = "text").text
            author_stuff = {"name" : author, "bio page" : bio_path, "quote" : text}
            quote_list.append(author_stuff)


        next_page = soup.find("li", class_ = "next")
        
        if next_page:
            next_path = next_page.find("a")["href"]
            next_link = url + next_path
        else:
            break
    return quote_list

def get_author_bio(path):
    url = "http://quotes.toscrape.com"
    response = requests.get(url+path)
    soup = BeautifulSoup(response.text, "html.parser")
    born_date = soup.find("span", class_ = "author-born-date").text 
    born_location = soup.find("span", class_ = "author-born-location").text
    bio = born_date + " " + born_location
    return bio

def main():
    quote_list = quote_scraper()

    while True:
        selection = choice(quote_list)
        print(f"\nWho said this quote: " + selection["quote"] + "\n")
        guesses = 4
        while guesses > 0:
            print(f"Guesses remaining: {guesses}\n")
            guess = input()
            if guess.lower() == selection["name"].lower():
                print("\nYou are correct!\n")
                break
            else:
                guesses -= 1
                if guesses == 3:
                    bio = get_author_bio(selection["bio page"])
                    print(f"\nThe author was born on " + bio + "\n")
                elif guesses == 2:
                    first_initial = selection["name"][0]
                    print(f"\nThe author's first initial is " + first_initial + "\n")
                elif guesses == 1:
                    name_split = selection["name"].split()
                    last_initial = name_split[len(name_split) - 1][0]
                    print(f"\nThe author's last initial is " + last_initial + "\n")
        
        if guesses == 0:
            print("You are out of guesses. Sucks to suck!\n")
            name = selection["name"]
            print(f"The author's name was {name}\n")
            print("Try again!\n\n")

        while True:
            play_again = input("Do you want to play again? (y/n) ")
            if play_again.lower() == "y":
                break
            elif play_again.lower() == "n":
                return False
            else:
                print("Please enter a valid choice.\n")

main()
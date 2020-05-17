# first_web_scraper

This is a simple guessing game that scrapes HTML code from the site http://quotes.toscrape.com/ using the BeautifulSoup class from the bs4 Python library.
A quote from the site is presented, and the user has four guesses to guess the correct author of the quote.

After the first incorrect guess, the program fetches and prints the date and location of birth of the author.
After the second incorrect guess, the program provides the author's first initial.
After the third incorrect guess, the program provides the author's last initial.
If all guesses are used up and the author is not guessed correctly, the program provides the author's name.

If any guess is correct before the four guesses are used up, the program informs the user and asks them if they want to play again.

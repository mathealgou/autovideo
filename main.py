import os
import sys
from scraper import scrape
from scraper import search
from terminal import *

# A little introduction
introduction("Autovideo", "1.0")

# for testing's sake
#print(search("bacon"))
print("Enter a search term:")
term = input()
print(f"Searching for {term}...")
article = search(term)
print(article[1])
print("Is this the article you were looking for?")
answer = input()
if answer.lower() == "y":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Great!")
    #Procced to do the video
elif answer.lower() == "n":
    #Clear the terminal and restart the program
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Please try again.")
    os.execl(sys.executable, sys.executable, *sys.argv)


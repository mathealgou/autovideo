from scraper import *
import os
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def introduction(name, version, creator="Matheus Goulart"):
    print(f"{bcolors.OKGREEN}Autovideo {version} by {creator}{bcolors.ENDC}")

def search_article():
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
        return article
    elif answer.lower() == "n":
        #Clear the terminal and restart the program
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Please try again.")
        os.execl(sys.executable, sys.executable, *sys.argv)
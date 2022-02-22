from time import sleep
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
    print(f"{bcolors.OKGREEN}{name} {version} by {creator}{bcolors.ENDC}")

def search_article():
    ask("Enter a search term:")
    term = input()
    ask(f"Searching for {term}...")
    article = search(term)
    print(article[0])
    ask("Is this the article you were looking for? (y/n)")
    answer = input()
    if answer.lower() == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        statement("Great!")
        #Procced to do the video
        return article
    elif answer.lower() == "n":
        #Clear the terminal and restart the program
        clear()
        ask("Please try again.")
        sleep(1)
        restart()

def debug(string):
    print(f"DEBUG: {bcolors.WARNING}{string}{bcolors.ENDC}")

def ask(string):
    print(f"{bcolors.OKCYAN}{string}{bcolors.ENDC}")

def statement(string):
    print(f"{bcolors.OKGREEN}{string}{bcolors.ENDC}")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def error(string):
    print(f"ERROR: {bcolors.FAIL}{string}{bcolors.ENDC}")

def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)

def progress(done, total, length=20, string="", fill="█", empty=" "):

    # Calculate the percentage
    percent = (done / total) * 100

    # round to int
    percent = int(percent)

    # Calculate the amount of "hashes"
    hashes = fill * int(percent / 100 * length)

    # Calculate the amount of spaces
    spaces = empty * (length - len(hashes))

    # Print the progress bar

    print(f"|\r{hashes}{spaces}| {percent}%", end="")

    print(f"{bcolors.OKBLUE}{string}{bcolors.ENDC}")
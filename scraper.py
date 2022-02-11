import requests
from bs4 import BeautifulSoup
import re

def scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html5lib")

    ps = soup.find_all("p")
    result = []
    for p in ps:
        result.append(p.text)
    
    result = clean_text(result)

    return result

def clean_text(text):
    if type(text) is list:
        # DEBUG LINE
        print("is list")
        result = []
        for t in text:
            t = t.replace("\n", "")
            result.append(re.sub("[\[].*?[\]]", "", t))
        result = remove_white_space_from_list(result)
        return result
    elif type(text) is str:
        # DEBUG LINE
        print("is not list")
        result = re.sub("[\(\[].*?[\)\]]", "", t)
        return result
    else:
        return f"Error: clean_text() cannot clean data of type{type(text)}"

def search(term):
    #I'm not sure if this is the best way to do this
    url = f"https://en.wikipedia.org/wiki/{term}"
    return scrape(url)


def remove_white_space_from_list(list):
    result = []
    for item in list:
        if type(item) != str:
            return f"Error: remove_white_space_from_list() cannot remove white space from list of type {type(item)}"
        else:
            if item.strip() != "":
                result.append(item.strip())
    return result
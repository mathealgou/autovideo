import requests
from bs4 import BeautifulSoup
import re

def scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html5lib")

    
    #result = soup.prettify()

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
        return result
    elif type(text) is str:
        # DEBUG LINE
        print("is not list")
        result = re.sub("[\(\[].*?[\)\]]", "", t)
        return result
    else:
        return f"Error: clean_text() cannot clean data of type{type(text)}"
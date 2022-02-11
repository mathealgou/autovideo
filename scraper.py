import requests
from bs4 import BeautifulSoup

def scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html5lib")

    
    #result = soup.prettify()

    result = soup.find_all("p")
    result = result.prettify()

    return result
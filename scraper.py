import requests
from bs4 import BeautifulSoup
import re
import terminal as terminal
import os
from dotenv import load_dotenv


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

        result = []

        for t in text:
            if type(t) != str:
                return f"Error: clean_text() cannot clean text of type {type(t)}"
            else:
                # t = t.replace("\n", "")
                if t.strip() != "":
                    result.append(re.sub("[\[].*?[\]]", "", t))
        return result
    elif type(text) is str:
        result = re.sub("[\(\[].*?[\)\]]", "", t)
        return result
    else:
        return f"Error: clean_text() cannot clean data of type{type(text)}"


def search(term):
    # I'm not sure if this is the best way to do this
    url = f"https://en.wikipedia.org/wiki/{term}"
    return scrape(url)


def get_images(term, filename):
    load_dotenv()
    KEY = os.getenv("GOOGLE_IMAGES_KEY")
    ID = os.getenv("GOOGLE_IMAGES_ID")
    from google_images_search import GoogleImagesSearch

    # you can provide API key and CX using arguments,
    # or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
    gis = GoogleImagesSearch(KEY, ID)

    # define search params:
    _search_params = {
        'q': term,
        'num': 1,
        'safe': 'high'
    }

    # this will search and download:
    gis.search(search_params=_search_params,
               path_to_dir='./images', custom_image_name=filename)
# get_images("cat")

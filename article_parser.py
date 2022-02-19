from typing import List
import terminal as terminal

unimportant_words = ["of", "the", "he", "they", "she", "it", "a", "all", "none", "to", "and", "with", "a", "an", "the", "in", "on", "at", "for", "by", "from", "of", "with", "as", "well", "also", "or", "is"]

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
    return num

def normalize_words(words: List[str]):
    normalized_words = []
    for word in words:
        new_word = ''.join(e for e in word if e.isalnum())
        normalized_words.append(new_word.lower())
    return normalized_words


def find_relevant_words(words: List[str]):
    relevant_words = []
    for word in words:
        if word not in unimportant_words:
            relevant_words.append(word)
    normalized_words = normalize_words(relevant_words)
    most_frequent_word = most_frequent(normalized_words)
    return most_frequent_word

def parse_article(article: List[str]):
    parsed_article = []
    paragraph = article[0]
    words = paragraph.split(" ")
    relevant_words = find_relevant_words(words)
    duration = len(words) / 20
    parsed_paragraph = {
        "text": paragraph,
        "duration": duration,
        "words": words,
        "images": []
    }
    parsed_article.append(parsed_paragraph)

    return parsed_article

    #  
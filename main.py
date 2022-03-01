import terminal as terminal
import video as video
from article_parser import parse_article
import scraper

# A little introduction
terminal.introduction("Autovideo", "1.0")


terminal.ask("Enter a search term:")

term = input()

terminal.ask(f"Searching for {term}...")

article = terminal.search_article(term)

parsed_article = parse_article(article)

# Ask for custom filename
terminal.ask("Enter a filename:")

filename = input()

scraper.get_images(term, filename)

video.render(720, 1280, 1.0, 20, filename, parsed_article)

terminal.statement("Done!")

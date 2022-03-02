import terminal as terminal
import video as video
from article_parser import parse_article
import scraper

# A little introduction
terminal.introduction("Autovideo", "1.0")

terminal.ask("Enter a search term:")

term: str = input()

terminal.ask(f"Searching for {term}...")

article: list[str] = terminal.search_article(term)

parsed_article: list[dict] = parse_article(article)

# Ask for custom filename
terminal.ask("Enter a filename:")

filename: str = input()

terminal.statement("Downloading images...")

scraper.get_images(term, filename)

terminal.clear()

video.render(720, 1280, 1.0, 20, filename, parsed_article)

terminal.statement("Done!")

from ast import parse
import terminal as terminal
import video as video
from article_parser import parse_article

# A little introduction
terminal.introduction("Autovideo", "1.0")

article = terminal.search_article()

terminal.debug("Rendering video...")

parsed_article = parse_article(article)

print(parsed_article)

video.render(720, 1280, 24, 20, "bacon", parsed_article)

terminal.statement("Done!")
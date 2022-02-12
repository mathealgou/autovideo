import terminal as terminal
import video as video

# A little introduction
terminal.introduction("Autovideo", "1.0")

article = terminal.search_article()

terminal.debug("Rendering video...")
video.render(720, 1280, 24, 20, "bacon")


terminal.statement("Done!")
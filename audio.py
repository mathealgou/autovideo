import pyttsx3

def create_audio_file(text):
    engine = pyttsx3.init()
    engine.save_to_file(text , 'test.mp3')
    engine.runAndWait()
    engine.stop()

create_audio_file("OH, boy")

# engine = pyttsx3.init()
# engine.runAndWait()
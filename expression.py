import pyttsx3

def speak(text):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Select the first voice
    engine.setProperty('rate', 180)
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()
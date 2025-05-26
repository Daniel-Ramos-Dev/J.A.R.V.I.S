import pyttsx3

def falar(texto):
    print("Jarvis:", texto)
    engine = pyttsx3.init()
    engine.setProperty("rate", 160)
    engine.say(texto)
    engine.runAndWait()

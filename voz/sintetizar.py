import pyttsx3

def falar(texto):
    engine = pyttsx3.init()
    engine.setProperty("rate", 175)  # Velocidade da fala
    engine.setProperty("volume", 1.0)  # Volume (0.0 a 1.0)
    engine.say(texto)
    engine.runAndWait()

def falar_e_desligar():
    falar("Desligando, senhor...")

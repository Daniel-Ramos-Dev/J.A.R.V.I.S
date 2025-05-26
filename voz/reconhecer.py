import speech_recognition as sr

def ouvir():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Você: (estou ouvindo...)")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio, language="pt-BR")
    except:
        return ""

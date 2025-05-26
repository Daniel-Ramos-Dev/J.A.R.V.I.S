import speech_recognition as sr
import os

def ouvir(arquivo_wav=None):
    r = sr.Recognizer()

    try:
        if arquivo_wav and os.path.isfile(arquivo_wav):
            with sr.AudioFile(arquivo_wav) as source:
                audio = r.record(source)
        else:
            with sr.Microphone() as source:
                print("Ouvindo pelo microfone...")
                audio = r.listen(source)

        return r.recognize_google(audio, language="pt-BR")
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return "Erro ao acessar o serviço de reconhecimento de voz."

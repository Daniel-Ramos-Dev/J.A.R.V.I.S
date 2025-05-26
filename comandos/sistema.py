import os

def executar_comando(texto):
    if "navegador" in texto:
        os.system("start chrome")
    elif "vscode" in texto or "visual studio" in texto:
        os.system("code")
    elif "terminal" in texto:
        os.system("start cmd")
    else:
        print("Comando desconhecido.")

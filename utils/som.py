from playsound import playsound

def tocar_som(caminho_arquivo):
    try:
        playsound(caminho_arquivo)
    except Exception as e:
        print(f"Erro ao tocar som: {e}")

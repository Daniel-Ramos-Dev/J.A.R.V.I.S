import os
import sys
from voz.sintetizar import falar_e_desligar

def verificar_e_executar(pergunta, resposta):
    comando = resposta.lower()

    if "abrir navegador" in comando:
        os.system("start chrome")
    elif "abrir vs code" in comando:
        os.system("code")
    elif "terminal" in comando:
        os.system("start cmd")
    elif "desligar" in comando or "encerrar" in comando or "fechar jarvis" in comando:
        falar_e_desligar()
        sys.exit()

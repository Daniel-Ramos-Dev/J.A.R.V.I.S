from voz.reconhecer import ouvir
from ia.conversar import responder
from comandos.sistema import executar_comando
from utils.interpretador import interpretar_comando
from utils.som import tocar_som
import time

CAMINHO_INICIAR = r"C:\Users\marga\OneDrive\Documentos\A.L.C\J.A.R.V.I.S\sons\iniciar.wav"
CAMINHO_ENCERRAR = r"C:\Users\marga\OneDrive\Documentos\A.L.C\J.A.R.V.I.S\sons\encerrar.wav"

def standby_ate_ativar():
    print("JARVIS em modo de espera. Diga 'ativar jarvis' para começar.")
    while True:
        frase = ouvir(CAMINHO_INICIAR).lower()  # Ouve arquivo .wav para ativar
        if "jarvis" in frase or "ativar" in frase:
            tocar_som(CAMINHO_INICIAR)  # Som de confirmação (opcional)
            print("JARVIS ativado.")
            break
        time.sleep(1)

def main():
    standby_ate_ativar()

    while True:
        texto = ouvir().lower()
        if not texto:
            continue

        if any(palavra in texto for palavra in ["encerrar", "desligar", "fechar jarvis"]):
            print("Encerrando o JARVIS...")
            tocar_som(CAMINHO_ENCERRAR)
            break

        if interpretar_comando(texto):
            executar_comando(texto)
        else:
            resposta = responder(texto)
            print("JARVIS:", resposta)

if __name__ == "__main__":
    main()

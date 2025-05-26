from voz.reconhecer import ouvir
from ia.conversar import responder
from comandos.sistema import executar_comando
from comandos.programar import executar_codigo
from voz.sintetizar import falar
from utils.interpretador import interpretar

def main():
    while True:
        texto = ouvir()
        if not texto:
            continue

        resposta = responder(texto)
        tipo, conteudo = interpretar(resposta)

        if tipo == "comando":
            executar_comando(conteudo)
        elif tipo == "codigo":
            executar_codigo(conteudo)
        else:
            falar(resposta)

if __name__ == "__main__":
    main()

def executar_codigo(codigo):
    try:
        exec(codigo)
    except Exception as e:
        print("Erro ao executar código:", e)

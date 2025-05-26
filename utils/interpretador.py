def interpretar(texto):
    if "def " in texto or "import" in texto:
        return "codigo", texto
    elif "abrir" in texto or "executar" in texto:
        return "comando", texto
    else:
        return "fala", texto

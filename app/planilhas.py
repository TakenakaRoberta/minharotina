
def padronizar_nome_completo(nome_nao_padronizado):
    nome = nome_nao_padronizado.upper().strip()
    while True:
        nome = nome.replace("  ", " ")
        if "  " not in nome:
            break
    return nome

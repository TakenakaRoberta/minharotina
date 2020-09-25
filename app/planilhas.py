
def padronizar_nome_completo(nome_completo_despadronizados):
    """
    Padroniza um nome completo:
    - removendo os espaços no início e no fim
    - removendo espaços extras entre os nomes
    - colocando em maiúsculas, inclusive nomes acentuados
    """
    padronizado = nome_completo_despadronizados.strip()
    padronizado = padronizado.upper()
    while True:
        padronizado = padronizado.replace(" "*2, " ")
        if "  " not in padronizado:
            break
    return padronizado


if __name__ == "__main__":
    nome = padronizar_nome_completo("Roberta")
    print(nome)

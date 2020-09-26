from unittest import TestCase
from app.planilhas import padronizar_nome_completo


class TestPadronizarNomeCompleto(TestCase):

    def test_padronizar_nome_completo_retorna_nome_em_letras_maiusculas(self):
        resultado = padronizar_nome_completo("ana")
        self.assertEqual("ANA", resultado)

    def test_padronizar_nome_completo_retorna_nome_sem_espacos_iniciais_e_finais(self):
        resultado = padronizar_nome_completo(" ANA ")
        self.assertEqual("ANA", resultado)

    # def test_padronizar_nome_completo_retorna_nome_sem_espacos_extras_entre_os_nomes(self):
    #     resultado = padronizar_nome_completo("ANA  PAULA")
    #     self.assertEqual("ANA PAULA", resultado)

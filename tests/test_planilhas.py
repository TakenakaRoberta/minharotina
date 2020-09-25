from unittest import TestCase
from app.planilhas import padronizar_nome_completo


class TestPadronizarNomeCompleto(TestCase):

    def test_padronizar_nome_completo_retorna_nome_sem_espacos_extras_no_inicio_e_no_fim(self):
        resultado = padronizar_nome_completo("    ANA   \t\n")
        self.assertEqual("ANA", resultado)

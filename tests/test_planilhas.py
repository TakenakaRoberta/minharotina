from unittest import TestCase
from app.planilhas import padronizar_nome_completo


class TestPadronizarNomeCompleto(TestCase):

    def test_padronizar_nome_completo_retorna_nome_sem_espacos_extras_no_inicio_e_no_fim(self):
        resultado = padronizar_nome_completo("    ANA   \t\n")
        self.assertEqual("ANA", resultado)

    def test_padronizar_nome_completo_retorna_nome_em_letras_maiusculas(self):
        resultado = padronizar_nome_completo("maria")
        self.assertEqual("MARIA", resultado)

    def test_padronizar_nome_completo_retorna_nome_separado_por_apenas_um_espaco(self):
        resultado = padronizar_nome_completo("Ana  Maria")
        self.assertEqual("ANA MARIA", resultado)

    def test_padronizar_nome_completo_retorna_nome_separado_por_apenas_um_espaco_se_o_nome_contiver_tres_espacos(self):
        resultado = padronizar_nome_completo("Ana   Maria")
        self.assertEqual("ANA MARIA", resultado)

    def test_padronizar_nome_completo_retorna_nome_separado_por_apenas_um_espaco_se_o_nome_contiver_quatro_espacos(self):
        resultado = padronizar_nome_completo("Ana" + " "*4 + "Maria")
        self.assertEqual("ANA MARIA", resultado)

    def test_padronizar_nome_completo_retorna_nome_padronizado_com_acentuacao(self):
        resultado = padronizar_nome_completo("Patrícia")
        self.assertEqual("PATRÍCIA", resultado)

    def test_padronizar_nome_completo_retorna_nome_padronizado_com_til(self):
        resultado = padronizar_nome_completo("João")
        self.assertEqual("JOÃO", resultado)

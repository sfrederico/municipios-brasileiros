from typing import List

from app.dao.populacao_dao import PopulacaoDAO
from app.db import get_db
from app.models.populacao import Populacao


class PopulacaoRepository:
    """Repository para operações de negócio relacionadas a municípios"""


    def __init__(self):
        self.populacao_dao = PopulacaoDAO(get_db())


    def listar_nao_capitais_mais_populosos(self):
        return self.populacao_dao.get_all_cidades_nao_capitais()
    
    def buscar_populacao_por_estado(self, uf: str) -> List[Populacao]:
        if not uf or len(uf.strip()) < 2:
            raise ValueError("O estado deve ter pelo menos 2 caracteres")
        """
        Busca a população de um estado específico.
        :param uf: Sigla do estado (ex: 'SP', 'RJ')
        :return: Lista de municípios com suas populações
        """
        return self.populacao_dao.get_populacao_por_estado(uf)
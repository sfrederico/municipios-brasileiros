from typing import List

from app.dao import MunicipioDAO
from app.db import get_db
from app.models import Municipio


class MunicipioRepository:
    """Repository para operações de negócio relacionadas a municípios"""

    def __init__(self):
        self.municipio_dao = MunicipioDAO(get_db())

    def buscar_por_nome(self, nome: str) -> List[Municipio]:
        """Busca municípios pelo nome (busca parcial)"""
        if not nome or len(nome.strip()) < 2:
            raise ValueError("Nome deve ter pelo menos 2 caracteres")

        nome = nome.strip()
        return self.municipio_dao.filter_by(nome_municipio=nome)

    def buscar_por_range_populacao(
        self, populacao_min: int, populacao_max: int
    ) -> List[Municipio]:
        """Busca municípios por faixa de população"""
        if populacao_min < 0 or populacao_max < 0:
            raise ValueError("População não pode ser negativa")
        if populacao_min > populacao_max:
            raise ValueError("População mínima não pode ser maior que a máxima")

        return self.municipio_dao.get_by_population_range(populacao_min, populacao_max)

    def buscar_dez_mais_populosos_nao_capitais(self) -> List[Municipio]:
        """Busca os dez municípios mais populosos que não são capitais"""
        return self.municipio_dao.get_top_non_capital_municipalities(10)

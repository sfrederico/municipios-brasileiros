from typing import List

from app.dao import MunicipioDAO
from app.dao.capital_dao import CapitalDAO
from app.db import get_db
from app.models import Municipio


class MunicipioRepository:
    """Repository para operações de negócio relacionadas a municípios"""

    def __init__(self):
        self.municipio_dao = MunicipioDAO(get_db())
        self.capital_dao = CapitalDAO(get_db())

    def buscar_por_nome(self, nome: str) -> List[Municipio]:
        """Busca municípios pelo nome (busca parcial)"""
        if not nome or len(nome.strip()) < 2:
            raise ValueError("Nome deve ter pelo menos 2 caracteres")

        nome = nome.strip()
        return self.municipio_dao.filter_by(nome_municipio=nome)

    def listar_capitais(self):
        return self.capital_dao.get_all_capitais()
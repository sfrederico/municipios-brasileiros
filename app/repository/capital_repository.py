from typing import List

from app.dao.capital_dao import CapitalDAO
from app.db import get_db
from app.models.capital import Capital


class CapitalRepository:
    """Repository para operações de negócio relacionadas a municípios"""

    def __init__(self):
        self.capitais_dao = CapitalDAO(get_db())

    def buscar_todas_capitais(self) -> List[Capital]:
        """Busca todas as capitais do Brasil"""
        return self.capitais_dao.get_all_capitais()

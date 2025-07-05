from typing import List

from app.dao.capital_dao import CapitalDAO
from app.db import get_db


class CapitalRepository:
    """Repository para operações de negócio relacionadas a municípios"""

    def __init__(self):
        self.capitais_dao = CapitalDAO(get_db())


    def listar_capitais(self):
        return self.capitais_dao.get_all_capitais()
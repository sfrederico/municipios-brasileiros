from typing import List, Optional

import psycopg2

from app.models.capital import Capital


class CapitalDAO:
    """DAO para operações de acesso aos dados de Município"""

    def __init__(self, connection):
        self.connection = connection


    def _row_to_municipio(self, row) -> Capital:
        """Converte uma linha do banco em objeto Capital"""
        return Capital(
            id=row[0],
            uf=row[1],
            cod_uf=row[2],
            cod_municipio=row[3],
            nome_municipio=row[4],
            populacao=row[6],
        )

    def get_all_capitais(self) -> List[Capital]:
        """Retorna todos os municípios que são capitais de estados"""
        query = "SELECT * FROM municipios WHERE capital_estado = ' Sim'"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                return [self._row_to_municipio(row) for row in rows]
        except psycopg2.Error as e:
            raise Exception(f"Erro ao buscar capitais: {e}")

from typing import List

import psycopg2

from app.models.populacao import Populacao


class PopulacaoDAO:
    """DAO para operações de acesso aos dados de Município"""

    def __init__(self, connection):
        self.connection = connection


    def _row_to_populacao(self, row) -> Populacao:
        """Converte uma linha do banco em objeto Capital"""
        return Populacao(
            id=row[0],
            uf=row[1],
            cod_uf=row[2],
            cod_municipio=row[3],
            nome_municipio=row[4],
            capital_estado=row[5],
            populacao=row[6],
        )

    def get_all_cidades_nao_capitais(self) -> List[Populacao]:
        """Retorna todos os municípios que são capitais de estados"""
        query = """
                SELECT m.*
                FROM municipios m
                JOIN municipios cap
                    ON m.uf = cap.uf
                AND cap.capital_estado = ' Sim'
                WHERE m.capital_estado = ' Não'
                AND m.populacao > cap.populacao;
                """
        
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                return [self._row_to_populacao(row) for row in rows]
        except psycopg2.Error as e:
            raise Exception(f"Erro ao buscar cidades não capitais: {e}")
        
    def get_populacao_por_estado(self, uf: str) -> List[Populacao]:
        """Busca a população de um estado específico."""
        query = """
                SELECT * FROM municipios
                WHERE uf = %s
                ORDER BY populacao DESC;
                """
        
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (uf,))
                rows = cursor.fetchall()
                return [self._row_to_populacao(row) for row in rows]
        except psycopg2.Error as e:
            raise Exception(f"Erro ao buscar população por estado: {e}")









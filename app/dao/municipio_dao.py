from typing import List, Optional

import psycopg2

from app.models.municipio import Municipio


class MunicipioDAO:
    """DAO para operações de acesso aos dados de Município"""

    def __init__(self, connection):
        self.connection = connection

    def get_by_id(self, municipio_id: int) -> Optional[Municipio]:
        """Busca um município pelo ID"""
        query = "SELECT * FROM municipios WHERE id = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (municipio_id,))
                row = cursor.fetchone()
                return self._row_to_municipio(row) if row else None
        except psycopg2.Error as e:
            raise Exception(f"Erro ao buscar município por ID: {e}")

    def get_all(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> List[Municipio]:
        """Retorna todos os municípios com paginação opcional"""
        query = "SELECT * FROM municipios ORDER BY nome_municipio"
        params = []

        if limit:
            query += " LIMIT %s"
            params.append(limit)

        if offset:
            query += " OFFSET %s"
            params.append(offset)

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                rows = cursor.fetchall()
                return [self._row_to_municipio(row) for row in rows]
        except psycopg2.Error as e:
            raise Exception(f"Erro ao buscar todos os municípios: {e}")

    def filter_by(self, **kwargs) -> List[Municipio]:
        """Filtra municípios por critérios específicos"""
        conditions = []
        params = []

        for key, value in kwargs.items():
            if value is not None:
                if key == "nome_municipio" and isinstance(value, str):
                    # Busca parcial para nome
                    conditions.append(f"{key} ILIKE %s")
                    params.append(f"%{value}%")
                else:
                    conditions.append(f"{key} = %s")
                    params.append(value)

        if not conditions:
            return self.get_all()

        query = f"SELECT * FROM municipios WHERE {' AND '.join(conditions)} ORDER BY nome_municipio"

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                rows = cursor.fetchall()
                return [self._row_to_municipio(row) for row in rows]
        except psycopg2.Error as e:
            raise Exception(f"Erro ao filtrar municípios: {e}")

    def count(self, **kwargs) -> int:
        """Retorna o total de municípios com filtros opcionais"""
        conditions = []
        params = []

        for key, value in kwargs.items():
            if value is not None:
                conditions.append(f"{key} = %s")
                params.append(value)

        query = "SELECT COUNT(*) FROM municipios"
        if conditions:
            query += f" WHERE {' AND '.join(conditions)}"

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchone()[0]
        except psycopg2.Error as e:
            raise Exception(f"Erro ao contar municípios: {e}")

    def exists(self, municipio_id: int) -> bool:
        """Verifica se um município existe pelo ID"""
        query = "SELECT 1 FROM municipios WHERE id = %s LIMIT 1"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (municipio_id,))
                return cursor.fetchone() is not None
        except psycopg2.Error as e:
            raise Exception(f"Erro ao verificar existência do município: {e}")

    def get_by_codigo(self, cod_municipio: int, cod_uf: int) -> Optional[Municipio]:
        """Busca município pelos códigos oficial"""
        query = "SELECT * FROM municipios WHERE cod_municipio = %s AND cod_uf = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (cod_municipio, cod_uf))
                row = cursor.fetchone()
                return self._row_to_municipio(row) if row else None
        except psycopg2.Error as e:
            raise Exception(f"Erro ao buscar município por código: {e}")

    def _row_to_municipio(self, row) -> Municipio:
        """Converte uma linha do banco em objeto Municipio"""
        return Municipio(
            id=row[0],
            uf=row[1],
            cod_uf=row[2],
            cod_municipio=row[3],
            nome_municipio=row[4],
            capital_estado=row[5],
            populacao=row[6],
        )

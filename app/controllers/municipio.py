from flask import render_template

from app.repository import MunicipioRepository


class MunicipioController:
    @staticmethod
    def buscar_municipio_por_nome(nome_municipio: str):
        municipios = MunicipioRepository().buscar_por_nome(nome_municipio)
        template = render_template(
            "listagem_municipios.html",
            municipios=municipios,
            titulo=f"Resultados para '{nome_municipio}'",
            descricao="Busca por nome de município",
        )
        return template

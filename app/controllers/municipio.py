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

    @staticmethod
    def buscar_municipio_por_range_populacao(populacao_min: int, populacao_max: int):
        municipios = MunicipioRepository().buscar_por_range_populacao(
            populacao_min, populacao_max
        )
        template = render_template(
            "listagem_municipios.html",
            municipios=municipios,
            titulo=f"Resultados para população entre {populacao_min} e {populacao_max}",
            descricao="Busca por faixa de população",
        )
        return template

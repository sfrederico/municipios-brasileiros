from app.controllers.home import HomeController
from app.controllers.municipio import MunicipioController


def register_routes(app):
    app.add_url_rule("/", "index", HomeController.index)
    app.add_url_rule(
        "/municipios-por-nome/<string:nome_municipio>",
        "buscar_municipio_por_nome",
        MunicipioController.buscar_municipio_por_nome,
    )

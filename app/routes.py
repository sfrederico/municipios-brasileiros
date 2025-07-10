from app.controllers.capital import CapitalController
from app.controllers.home import HomeController
from app.controllers.municipio import MunicipioController
from app.controllers.populacao import PopulacaoController


def register_routes(app):
    app.add_url_rule("/", "index", HomeController.index)
    
    app.add_url_rule(
        "/municipios-por-nome/<string:nome_municipio>",
        "buscar_municipio_por_nome",
        MunicipioController.buscar_municipio_por_nome,
    )
    app.add_url_rule(
        "/municipios-por-range-populacao/<int:populacao_min>/<int:populacao_max>",
        "buscar_municipio_por_range_populacao",
        MunicipioController.buscar_municipio_por_range_populacao,
    )
    app.add_url_rule("/capitais", 
                     "listar_capitais", 
                     CapitalController.listar_capitais_controller)
    
    app.add_url_rule("/cidades-nao-capitais-mais-populosas", 
                     "listar_nao_capitais_mais_populosos", 
                     PopulacaoController.listar_nao_capitais_mais_populosos_controller)
    
    app.add_url_rule("/buscar-populacao-por-estado/<string:uf>", 
                     "buscar_populacao_por_estado", 
                     PopulacaoController.buscar_populacao_por_estado_controller)
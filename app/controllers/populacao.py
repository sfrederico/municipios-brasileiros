from flask import render_template

from app.repository.populacao_repository import PopulacaoRepository


class PopulacaoController:
    @staticmethod
    def listar_nao_capitais_mais_populosos_controller():
        cidades_nao_capitais = PopulacaoRepository().listar_nao_capitais_mais_populosos()
        return render_template('listagem_cidades_nao_capitais.html', 
                               cidades=cidades_nao_capitais, 
                               titulo="Cidades não capitais mais populosas", 
                               descricao="Listagem de cidades não capitais mais populosas")
    @staticmethod
    def buscar_populacao_por_estado_controller(uf):
        uf = uf.strip().upper()
        estado = PopulacaoRepository().buscar_populacao_por_estado(uf)
        populacao_total = sum(c.populacao for c in estado)

        template = render_template('listagem_populacao_estados.html', 
                               uf=uf, 
                               estado=estado,
                               populacao_total=populacao_total,
                               titulo="População por Estado", 
                               descricao="Mostra a População de um estado")
        return template
    
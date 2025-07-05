from flask import render_template

from app.repository.capital_repository import CapitalRepository
from app.repository.municipio_repository import MunicipioRepository


class CapitalController:
    @staticmethod
    def listar_capitais_controller():
        capitais = MunicipioRepository().listar_capitais()
        return render_template('listagem_capital.html', capitais=capitais)
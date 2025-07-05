from flask import render_template

from app.repository.capital_repository import CapitalRepository


class CapitalController:
    @staticmethod
    def listar_capitais_controller():
        capitais = CapitalRepository().listar_capitais()
        return render_template('listagem_capital.html', capitais=capitais)